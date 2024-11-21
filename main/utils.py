from datetime import datetime,timedelta,timezone

def human_time_difference(from_time:datetime, to_time:datetime|None =None ) -> str:
    if to_time is None:
        to_time = datetime.now(tz=timezone.utc)
    
    # Calculate the time difference
    td :timedelta=  to_time - from_time

    if td.days >= 7:
        weeks = td.days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif td.days > 0:
        return f"{td.days} day{'s' if td.days > 1 else ''} ago"
    else:
        hours = td.seconds // 3600
        if hours > 0:
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        else:
            minutes = td.seconds // 60
            if minutes > 0:
                return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            else:
                return f"{td.seconds} second{'s' if td.seconds > 1 else ''} ago"


