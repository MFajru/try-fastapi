"""update model relation

Revision ID: b3c1868cc99f
Revises: c7ec4a9f5899
Create Date: 2024-12-02 10:37:37.840738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c1868cc99f'
down_revision: Union[str, None] = 'c7ec4a9f5899'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
