# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('places_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home_address', self.gf('django.db.models.fields.TextField')()),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('places', ['UserProfile'])

        # Adding model 'Category'
        db.create_table('places_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('places', ['Category'])

        # Adding model 'Place'
        db.create_table('places_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zipcode', self.gf('django.db.models.fields.IntegerField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Greece', max_length=50)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('action', self.gf('django.db.models.fields.CharField')(default='', max_length=1)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['places.Category'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('places', ['Place'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('places_userprofile')

        # Deleting model 'Category'
        db.delete_table('places_category')

        # Deleting model 'Place'
        db.delete_table('places_place')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'places.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'places.place': {
            'Meta': {'object_name': 'Place'},
            'action': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['places.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Greece'", 'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {})
        },
        'places.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'home_address': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['places']
