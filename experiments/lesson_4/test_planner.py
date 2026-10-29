import pytest
from .planner import save_events_for_date

class OSInterfaceFake(list):
    
    def read(self, path: str) -> list[str]:
        return ['1 task']
    
    def write(self, path, scope) -> bool:
        self.extend(scope)
        return self

def test_have_today_event():
    date = 1
    current_event = ['1 task']
    db = OSInterfaceFake() 
    
    event = save_events_for_date(session=db, date=1, m_path='path', d_path='path')
    assert event == current_event
    