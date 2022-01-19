import csv
from io import StringIO
from flask import flash, redirect, render_template, Response, url_for

from . import home
from .forms import InventoryForm
from .. import db
from ..models import Inventory

# Inventory Views

@home.route('/', methods=['GET', 'POST'])
def list_inventory():
  """
  List all inventory
  """

  inventory = Inventory.query.all()

  return render_template(
    'home/inventory.html',
    inventory=inventory,
    title="Shopify Challenge"
  )

@home.route('/add', methods=['GET', 'POST'])
def add_item():
  """
  Add an item to the database
  """

  add_item = True

  form = InventoryForm()
  if form.validate_on_submit():
    item = Inventory(
      item=form.item.data,
      description=form.description.data,
      quantity=form.quantity.data
    )
    try:
      # add item to the database
      db.session.add(item)
      db.session.commit()
      flash('You have successfully added a new item.')
    except:
      # in case item name already exists
      flash('Error: item name already exists.')

    # redirect to inventory page
    return redirect(url_for('home.list_inventory'))

  # load item template
  return render_template(
    'home/item.html',
    action="Add",
    add_item=add_item,
    form=form,
    title="Add Item"
  )

@home.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
  """
  Edit an item
  """

  add_item = False

  item = Inventory.query.get_or_404(id)
  form = InventoryForm(obj=item)
  if form.validate_on_submit():
    item.item = form.item.data
    item.description = form.description.data
    item.quantity = form.quantity.data
    db.session.commit()
    flash('You have successfully edited the item.')

    # redirect to the inventory page
    return redirect(url_for('home.list_inventory'))

  form.item.data = item.item
  form.description.data = item.description
  form.quantity.data = item.quantity
  return render_template(
    'home/item.html',
    action="Edit",
    add_item=add_item,
    form=form,
    item=item,
    title="Edit Item"
  )

@home.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_item(id):
  """
  Delete an item from the database
  """

  item = Inventory.query.get_or_404(id)
  db.session.delete(item)
  db.session.commit()
  flash('You have successfully deleted the item.')

  # redirect to the inventory page
  return redirect(url_for('home.list_inventory'))


# File export

@home.route('/export/csv', methods=['GET', 'POST'])
def export_csv():
  """
  Export intventory items to CSV
  """

  inventory = Inventory.query.all()

  def generate():
    data = StringIO()
    w = csv.writer(data)

    # write header
    w.writerow(('item', 'description', 'quantity'))
    yield data.getvalue()
    data.seek(0)
    data.truncate(0)

    for item in inventory:
      w.writerow((
        item.item,
        item.description,
        item.quantity
      ))
      yield data.getvalue()
      data.seek(0)
      data.truncate(0)
  
  # stream the response as the data is generated
  response = Response(
    generate(),
    mimetype='text/csv',
    headers={"Content-disposition": "attachment; filename=inventory.csv"}
  )
  return response
