"""image column

Revision ID: c53836e0de56
Revises: 31c7fbb481a2
Create Date: 2023-08-26 13:19:03.554304

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c53836e0de56"
down_revision = "31c7fbb481a2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("event", sa.Column("image", sa.String(), nullable=True))
    op.add_column("tour", sa.Column("image", sa.String(), nullable=True))
    op.add_column("university", sa.Column("image", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("university", "image")
    op.drop_column("tour", "image")
    op.drop_column("event", "image")
    # ### end Alembic commands ###