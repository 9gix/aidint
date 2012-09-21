# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cause'
        db.create_table('project_cause', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('project', ['Cause'])

        # Adding model 'Photo'
        db.create_table('project_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('original', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('cause', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Cause'])),
        ))
        db.send_create_signal('project', ['Photo'])

        # Adding model 'Project'
        db.create_table('project_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('budget', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('begin_on', self.gf('django.db.models.fields.DateField')()),
            ('end_on', self.gf('django.db.models.fields.DateField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('project', ['Project'])

        # Adding M2M table for field causes on 'Project'
        db.create_table('project_project_causes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['project.project'], null=False)),
            ('cause', models.ForeignKey(orm['project.cause'], null=False))
        ))
        db.create_unique('project_project_causes', ['project_id', 'cause_id'])


    def backwards(self, orm):
        # Deleting model 'Cause'
        db.delete_table('project_cause')

        # Deleting model 'Photo'
        db.delete_table('project_photo')

        # Deleting model 'Project'
        db.delete_table('project_project')

        # Removing M2M table for field causes on 'Project'
        db.delete_table('project_project_causes')


    models = {
        'project.cause': {
            'Meta': {'object_name': 'Cause'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'project.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cause': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Cause']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'project.project': {
            'Meta': {'object_name': 'Project'},
            'begin_on': ('django.db.models.fields.DateField', [], {}),
            'budget': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'causes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['project.Cause']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_on': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['project']