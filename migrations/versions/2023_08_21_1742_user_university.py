"""user_university

Revision ID: 31c7fbb481a2
Revises: c8be85d65159
Create Date: 2023-08-21 17:42:29.499744

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "31c7fbb481a2"
down_revision = "c8be85d65159"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_university",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("university_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["university_id"],
            ["university.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_university")
    # ### end Alembic commands ###
