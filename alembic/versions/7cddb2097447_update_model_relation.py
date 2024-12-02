"""update model relation

Revision ID: 7cddb2097447
Revises: c636a37d03b3
Create Date: 2024-12-02 10:41:10.092561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cddb2097447'
down_revision: Union[str, None] = 'c636a37d03b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
