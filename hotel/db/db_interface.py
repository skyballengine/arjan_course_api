from typing import Any, Protocol
from hotel.db.models import Base, to_dict
from hotel.db.engine import DBSession

DataObject = dict[str, Any]

# implements the DataInterface protocol
class DBInterface:
    def __init__(self, db_class: type[Base]):
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        return to_dict(result)

    def read_all(self) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).all()
        return [to_dict(r) for r in result]

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)
        session.add(result)
        session.commit()
        return to_dict(result)
    
    def update(self, id: int, data: DataObject):
        session = DBSession()
        result = session.query(self.db_class).get(id)
        for key, value in data.items():
            if value != None:
                setattr(result, key, value)
        session.commit()
        return to_dict(result)
    
    def delete_all(self) -> DataObject:
        session = DBSession()
        results = session.query(self.db_class).all()
        for r in results:
            session.delete(r)
        session.commit()
        return [to_dict(r) for r in results]

    def delete(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        session.delete(result)
        session.commit()
        return to_dict(result)