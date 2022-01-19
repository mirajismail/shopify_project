from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InventoryForm(FlaskForm):
  """
  Form to add or edit an inventory item
  """

  item = StringField('Item', validators=[DataRequired()])
  description = StringField('Description', validators=[DataRequired()])
  quantity = StringField('Quantity', validators=[DataRequired()])
  submit = SubmitField('Submit')
