"""empty message

Revision ID: 139caa0fd3af
Revises: 1f9bb05708b8
Create Date: 2023-06-07 02:57:19.239842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '139caa0fd3af'
down_revision = '1f9bb05708b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('cate',
               existing_type=sa.TEXT(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.alter_column('cate',
               existing_type=sa.TEXT(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
