def analyze_user_activity(log_file_path: str) -> dict:
    action_counts = {}
    user_total_duration = {}   
    login_durations_sum = 0    
    login_count = 0

    try:
        with open(log_file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 4:
                    continue

                _, user_id, action, duration_str = parts

                try:
                    duration = int(duration_str)
                except ValueError:
                    continue

                action_counts[action] = action_counts.get(action, 0) + 1

                user_total_duration[user_id] = user_total_duration.get(user_id, 0) + duration

                if action == "login":
                    login_durations_sum += duration
                    login_count += 1

        total_users = len(user_total_duration)

        most_active_user = None
        if user_total_duration:
            most_active_user = max(user_total_duration, key=user_total_duration.get)

        average_session_time = 0.0
        if login_count > 0:
            average_session_time = login_durations_sum / login_count

        return {
            "total_users": total_users,
            "action_counts": action_counts,
            "most_active_user": most_active_user,
            "average_session_time": float(f"{average_session_time:.2f}"),
        }

    except FileNotFoundError:
        return {
            "total_users": 0,
            "action_counts": {},
            "most_active_user": None,
            "average_session_time": 0.0,
        }