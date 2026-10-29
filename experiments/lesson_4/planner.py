# приложение которое проверяет календарь 
# и если есть задачи на сегодня то переносит его в план дня

daily_path = 'daily.txt'
month_path = 'month.txt'

class OSInterface:
   
    def read(self, path: str) -> list[str]:
        with open(path, 'r') as fm:
            return fm.lines()
    
    def write(self, path, scope) -> list[str]:
        with open(path, 'w') as fd:
            fd.writelines(scope)
        return scope

db = OSInterface()

def get_events(db, path: str, date: int) -> list[str]:
    tasks = []
    
    
    lines: list[str] = db.read(path)
    for line in lines:
        if line.startswith(str(date)):
            tasks.append(line)
    return tasks

def save_events(db, path: str, scope: list) -> list[str]:
    
    return db.write(path, scope)
    

def save_events_for_date(session, date, m_path, d_path,):
    events = get_events(session, m_path, date)
    if not events:
        return False
    
    saved_events = save_events(session, d_path, events)
    return saved_events
    
    
    