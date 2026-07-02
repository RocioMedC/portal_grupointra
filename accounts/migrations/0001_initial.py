from django.db import migrations

def crear_grupos_sistema_intra(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    roles = ['Terapeutas', 'Recepción', 'Administración', 'Dirección', 'Sistemas']
    
    for nombre_rol in roles:
        Group.objects.get_or_create(name=nombre_rol)

class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(crear_grupos_sistema_intra),
    ]