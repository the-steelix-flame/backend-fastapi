from app.models.order import Order


def create_order(db, data):
    order = Order(**data.model_dump())

    db.add(order)
    db.commit()
    db.refresh(order)

    return order