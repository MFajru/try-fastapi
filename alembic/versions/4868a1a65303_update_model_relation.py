"""update model relation

Revision ID: 4868a1a65303
Revises: 7cddb2097447
Create Date: 2024-12-02 10:43:44.683271

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4868a1a65303'
down_revision: Union[str, None] = '7cddb2097447'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
