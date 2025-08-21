from django.db import migrations, models


def create_items(apps, schema_editor):
    Item = apps.get_model('api', 'Item')
    Item.objects.create(name='Apples', quantity=5)
    Item.objects.create(name='Bananas', quantity=3)
    Item.objects.create(name='Cherries', quantity=8)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(create_items),
    ]
