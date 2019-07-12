"""empty message

Revision ID: b390b1a179ec
Revises: 6e01628c35e9
Create Date: 2018-06-01 14:40:20.296787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b390b1a179ec'
down_revision = '6e01628c35e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=128), nullable=True),
    sa.Column('s3_bucket', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_images',
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_images')
    op.drop_table('image')
    # ### end Alembic commands ###