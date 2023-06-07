"""empty message

Revision ID: 3383ad93e55f
Revises: 2c9954fcf6f6
Create Date: 2023-06-07 01:59:11.800811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3383ad93e55f'
down_revision = '2c9954fcf6f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###