from app import db

class Inventory(db.Model):
  """
  Create a Inventory table
  """

  __tablename__ = 'inventory'

  id = db.Column(db.Integer, primary_key=True)
  item = db.Column(db.String(60), unique=True)
  description = db.Column(db.String(200))
  quantity = db.Column(db.Integer)

  def __repr__(self):
    return '<Inventory: {}>'.format(self.item)
