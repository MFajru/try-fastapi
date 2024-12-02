"""update model relation

Revision ID: c7ec4a9f5899
Revises: 8983ab4742c4
Create Date: 2024-12-02 10:35:39.627293

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7ec4a9f5899'
down_revision: Union[str, None] = '8983ab4742c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
