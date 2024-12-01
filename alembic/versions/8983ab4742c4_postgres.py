"""postgres

Revision ID: 8983ab4742c4
Revises: 68096c7a6281
Create Date: 2024-11-30 07:54:09.889027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8983ab4742c4'
down_revision: Union[str, None] = '68096c7a6281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
