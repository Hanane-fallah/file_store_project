from core.models import DBModel
from core.manager import store_db


class File(DBModel):
    TABLE = "products"
    PK = "p_id"

    def __init__(self, id, path, up_date, mod_date, seller_id, show_name, desc, available=True, comment=None):
        self.id = id
        self.path = path
        self.up_date = up_date
        self.mod_date = mod_date
        self.seller_id = seller_id
        self.show_name = show_name
        self.desc = desc
        self.available = available
        self.comment = comment
        store_db.insert(File, "(id, file, upload_date, modify_date, seller_id, showname, description, available, comment)",
                        (self.id, self.path, self.up_date, self.mod_date, self.seller_id, self.show_name, self.desc, self.available, self.comment)
                        )
