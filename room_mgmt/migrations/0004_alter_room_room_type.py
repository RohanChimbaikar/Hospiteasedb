# Generated by Django 5.0.3 on 2024-04-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_mgmt', '0003_remove_room_room_types_room_room_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('ICU', 'Intensive Care Unit'), ('OR', 'Operating Room'), ('Maternity', 'Maternity Room'), ('Pediatric', 'Pediatric Room'), ('Emergency', 'Emergency Room'), ('Isolation', 'Isolation Room'), ('Recovery', 'Recovery Room'), ('Laboratory', 'Laboratory Room'), ('Radiology', 'Radiology Room'), ('Oncology', 'Oncology Room'), ('Hematology', 'Hematology Room'), ('Neurology', 'Neurology Room'), ('Cardiology', 'Cardiology Room'), ('Psychiatric', 'Psychiatric Room')], default='Regular', max_length=20),
        ),
    ]
