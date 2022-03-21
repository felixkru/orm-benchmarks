# Generated by Django 2.2.3 on 2019-07-29 19:22

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Journal1",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("level", models.SmallIntegerField(db_index=True)),
                ("text", models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Journal3",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("level", models.SmallIntegerField(db_index=True)),
                ("text", models.CharField(db_index=True, max_length=255)),
                ("col_float1", models.FloatField(default=2.2)),
                ("col_smallint1", models.SmallIntegerField(default=2)),
                ("col_int1", models.IntegerField(default=2000000)),
                ("col_bigint1", models.BigIntegerField(default=99999999)),
                ("col_char1", models.CharField(default="value1", max_length=255)),
                (
                    "col_text1",
                    models.TextField(default="Moo,Foo,Baa,Waa,Moo,Foo,Baa,Waa,Moo,Foo,Baa,Waa"),
                ),
                (
                    "col_decimal1",
                    models.DecimalField(decimal_places=8, default=Decimal("2.2"), max_digits=12),
                ),
                (
                    "col_json1",
                    models.JSONField(
                        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
                    ),
                ),
                ("col_float2", models.FloatField(null=True)),
                ("col_smallint2", models.SmallIntegerField(null=True)),
                ("col_int2", models.IntegerField(null=True)),
                ("col_bigint2", models.BigIntegerField(null=True)),
                ("col_char2", models.CharField(max_length=255, null=True)),
                ("col_text2", models.TextField(null=True)),
                (
                    "col_decimal2",
                    models.DecimalField(decimal_places=8, max_digits=12, null=True),
                ),
                ("col_json2", models.JSONField(null=True)),
                ("col_float3", models.FloatField(default=2.2)),
                ("col_smallint3", models.SmallIntegerField(default=2)),
                ("col_int3", models.IntegerField(default=2000000)),
                ("col_bigint3", models.BigIntegerField(default=99999999)),
                ("col_char3", models.CharField(default="value1", max_length=255)),
                (
                    "col_text3",
                    models.TextField(default="Moo,Foo,Baa,Waa,Moo,Foo,Baa,Waa,Moo,Foo,Baa,Waa"),
                ),
                (
                    "col_decimal3",
                    models.DecimalField(decimal_places=8, default=Decimal("2.2"), max_digits=12),
                ),
                (
                    "col_json3",
                    models.JSONField(
                        default={"a": 1, "b": "b", "c": [2], "d": {"e": 3}, "f": True}
                    ),
                ),
                ("col_float4", models.FloatField(null=True)),
                ("col_smallint4", models.SmallIntegerField(null=True)),
                ("col_int4", models.IntegerField(null=True)),
                ("col_bigint4", models.BigIntegerField(null=True)),
                ("col_char4", models.CharField(max_length=255, null=True)),
                ("col_text4", models.TextField(null=True)),
                (
                    "col_decimal4",
                    models.DecimalField(decimal_places=8, max_digits=12, null=True),
                ),
                ("col_json4", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Journal2",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("level", models.SmallIntegerField(db_index=True)),
                ("text", models.CharField(db_index=True, max_length=255)),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="simple.Journal2",
                    ),
                ),
                (
                    "related",
                    models.ManyToManyField(related_name="related_from", to="simple.Journal2"),
                ),
            ],
        ),
    ]
