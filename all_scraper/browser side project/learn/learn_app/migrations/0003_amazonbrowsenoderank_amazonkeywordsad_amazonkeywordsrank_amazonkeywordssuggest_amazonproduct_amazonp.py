# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn_app', '0002_auto_20170410_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonBrowseNodeRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('type', models.CharField(max_length=13)),
                ('department', models.CharField(max_length=32)),
                ('node_id', models.BigIntegerField()),
                ('rank', models.TextField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_browse_node_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonKeywordsAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('keywords', models.CharField(max_length=128)),
                ('node_id', models.BigIntegerField()),
                ('ad', models.TextField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_keywords_ad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonKeywordsRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('keywords', models.CharField(max_length=128)),
                ('node_id', models.BigIntegerField()),
                ('rank', models.TextField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_keywords_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonKeywordsSuggest',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('keywords_id', models.IntegerField()),
                ('parent_keywords_id', models.IntegerField()),
            ],
            options={
                'db_table': 'amazon_keywords_suggest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('asin', models.CharField(max_length=10)),
                ('variation_parentage', models.CharField(max_length=6)),
                ('parent_asin', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.IntegerField()),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('detail_page_url', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=64, null=True)),
                ('browse_node', models.CharField(blank=True, max_length=64, null=True)),
                ('sales_rank', models.IntegerField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('shipping', models.CharField(blank=True, max_length=64, null=True)),
                ('list_price', models.IntegerField(blank=True, null=True)),
                ('fulfillment', models.CharField(blank=True, max_length=3, null=True)),
                ('seller_id', models.CharField(blank=True, max_length=14, null=True)),
                ('seller_name', models.CharField(blank=True, max_length=64, null=True)),
                ('first_available_date', models.DateField(blank=True, null=True)),
                ('last_updated_time', models.DateTimeField()),
                ('bestseller_node_id', models.BigIntegerField(blank=True, null=True)),
                ('is_fba', models.IntegerField(blank=True, null=True)),
                ('offer_count', models.SmallIntegerField()),
                ('variation_count', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'amazon_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductImage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=6)),
                ('asin', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=128)),
                ('width', models.SmallIntegerField(blank=True, null=True)),
                ('height', models.SmallIntegerField(blank=True, null=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'db_table': 'amazon_product_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductKeywordsAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('asin', models.CharField(max_length=10)),
                ('keywords', models.CharField(max_length=128)),
                ('node_id', models.BigIntegerField()),
                ('position', models.SmallIntegerField()),
                ('page_id', models.SmallIntegerField()),
                ('page_position', models.SmallIntegerField()),
                ('ad_position_type', models.IntegerField()),
                ('ad_position', models.IntegerField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_product_keywords_ad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductKeywordsRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('asin', models.CharField(max_length=10)),
                ('keywords', models.CharField(max_length=128)),
                ('node_id', models.BigIntegerField()),
                ('rank', models.SmallIntegerField()),
                ('page_id', models.SmallIntegerField()),
                ('page_position', models.SmallIntegerField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_product_keywords_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('review_id', models.CharField(max_length=16)),
                ('asin', models.CharField(max_length=10)),
                ('customer_id', models.CharField(blank=True, max_length=16, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=64, null=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('helpful_yes', models.IntegerField(blank=True, null=True)),
                ('helpful_no', models.IntegerField(blank=True, null=True)),
                ('is_verified', models.IntegerField(blank=True, null=True)),
                ('is_image_included', models.IntegerField(blank=True, null=True)),
                ('is_video_included', models.IntegerField(blank=True, null=True)),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'amazon_product_review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductReviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('review_id', models.CharField(max_length=16)),
                ('url', models.CharField(max_length=128)),
                ('width', models.SmallIntegerField(blank=True, null=True)),
                ('height', models.SmallIntegerField(blank=True, null=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'db_table': 'amazon_product_review_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonProductReviewVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('review_id', models.CharField(max_length=16)),
                ('url', models.CharField(max_length=128)),
                ('image_url', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'amazon_product_review_video',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('seller_id', models.CharField(max_length=16)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=128, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('last_30_days_positive_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_90_days_positive_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_12_months_positive_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('lifetime_positive_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_30_days_neutral_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_90_days_neutral_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_12_months_neutral_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('lifetime_neutral_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_30_days_negative_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_90_days_negative_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_12_months_negative_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('lifetime_negative_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('last_30_days_feedback_count', models.IntegerField(blank=True, null=True)),
                ('last_90_days_feedback_count', models.IntegerField(blank=True, null=True)),
                ('last_12_months_feedback_count', models.IntegerField(blank=True, null=True)),
                ('lifetime_feedback_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'amazon_seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonSellerProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('seller_id', models.CharField(max_length=14)),
                ('asin', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('rank', models.SmallIntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('list_price', models.IntegerField(blank=True, null=True)),
                ('seller_name', models.CharField(blank=True, max_length=128, null=True)),
                ('seller_logo_url', models.CharField(blank=True, max_length=128, null=True)),
                ('seller_logo_width', models.SmallIntegerField(blank=True, null=True)),
                ('seller_logo_height', models.SmallIntegerField(blank=True, null=True)),
                ('seller_rating', models.IntegerField(blank=True, null=True)),
                ('seller_last_12_months_positive_feedback_ratio', models.IntegerField(blank=True, null=True)),
                ('seller_lifetime_feedback_count', models.IntegerField(blank=True, null=True)),
                ('search_index', models.CharField(blank=True, max_length=32, null=True)),
                ('bestseller_node_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'amazon_seller_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonSellerProductOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('seller_id', models.CharField(max_length=14)),
                ('asin', models.CharField(max_length=10)),
                ('item_id', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.IntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('shipping', models.CharField(blank=True, max_length=64, null=True)),
                ('condition', models.CharField(blank=True, max_length=21, null=True)),
                ('fulfillment', models.CharField(blank=True, max_length=3, null=True)),
                ('inventory', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'amazon_seller_product_offer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AmazonTopReviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('top_reviewer_id', models.CharField(max_length=16)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('rank', models.SmallIntegerField(blank=True, null=True)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('helpful_vote_count', models.IntegerField(blank=True, null=True)),
                ('helpful_vote_ratio', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'amazon_top_reviewer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DownloadQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_download_queue_id', models.IntegerField()),
                ('region', models.IntegerField()),
                ('type', models.IntegerField()),
                ('value', models.CharField(max_length=64)),
                ('status', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('scrape_count', models.IntegerField()),
                ('upload_status', models.IntegerField()),
                ('upload_count', models.IntegerField()),
                ('last_updated_time', models.DateTimeField(blank=True, null=True)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'download_queue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=128)),
                ('monthly_amazon_search_volume', models.IntegerField(blank=True, null=True)),
                ('amazon_product_search_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'keywords',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LearnAppPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30)),
                ('region', models.SmallIntegerField()),
                ('type', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'learn_app_person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('module', models.CharField(max_length=64)),
                ('priority', models.IntegerField()),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=8)),
                ('host', models.CharField(max_length=64)),
                ('port', models.SmallIntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=64, null=True)),
                ('password', models.CharField(blank=True, max_length=64, null=True)),
                ('count', models.IntegerField()),
                ('robot_check_count', models.IntegerField()),
                ('active_time', models.DateTimeField(blank=True, null=True)),
                ('inactive_time', models.DateTimeField(blank=True, null=True)),
                ('recover_failed_count', models.IntegerField(blank=True, null=True)),
                ('last_robot_check_url', models.CharField(blank=True, max_length=255, null=True)),
                ('last_robot_check_useragent_id', models.IntegerField(blank=True, null=True)),
                ('last_robot_check_time', models.DateTimeField(blank=True, null=True)),
                ('last_used_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'proxy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProxyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_id', models.SmallIntegerField()),
                ('region', models.SmallIntegerField()),
                ('status', models.CharField(max_length=8)),
                ('count', models.IntegerField()),
                ('robot_check_count', models.IntegerField()),
                ('active_time', models.DateTimeField(blank=True, null=True)),
                ('inactive_time', models.DateTimeField(blank=True, null=True)),
                ('recover_failed_count', models.IntegerField(blank=True, null=True)),
                ('last_robot_check_url', models.CharField(blank=True, max_length=255, null=True)),
                ('last_robot_check_useragent_id', models.IntegerField(blank=True, null=True)),
                ('last_robot_check_time', models.DateTimeField(blank=True, null=True)),
                ('last_used_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'proxy_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_queue_id', models.IntegerField()),
                ('method', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(max_length=255)),
                ('proxy_id', models.SmallIntegerField(blank=True, null=True)),
                ('begin_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'scrape',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UploadQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.IntegerField()),
                ('type', models.IntegerField()),
                ('value', models.CharField(max_length=64)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'upload_queue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Useragent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('robot_check_count', models.IntegerField()),
                ('last_used_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'useragent',
                'managed': False,
            },
        ),
    ]
