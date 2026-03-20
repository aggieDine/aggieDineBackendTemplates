import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.example import Item
from app.schemas.example import ItemCreate, ItemUpdate


async def create_item(db: AsyncSession, data: ItemCreate) -> Item:
    item = Item(**data.model_dump())
    db.add(item)
    await db.flush()
    await db.refresh(item)
    return item


async def get_item(db: AsyncSession, item_id: uuid.UUID) -> Item | None:
    return await db.get(Item, item_id)


async def list_items(db: AsyncSession, skip: int = 0, limit: int = 20) -> list[Item]:
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return list(result.scalars().all())


async def update_item(
    db: AsyncSession, item_id: uuid.UUID, data: ItemUpdate
) -> Item | None:
    item = await db.get(Item, item_id)
    if item is None:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(item, field, value)
    await db.flush()
    await db.refresh(item)
    return item


async def delete_item(db: AsyncSession, item_id: uuid.UUID) -> bool:
    item = await db.get(Item, item_id)
    if item is None:
        return False
    await db.delete(item)
    await db.flush()
    return True
