# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([('ImageHero', wagtail.wagtailcore.blocks.StructBlock([(b'hero_text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, required=False)), (b'hero_heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'link_location', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'hero_image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('TextHero', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True))])), ('FooterHero', wagtail.wagtailcore.blocks.StructBlock([(b'footer_text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), (b'footer_image', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('ImageSlideHero', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'slide', wagtail.wagtailcore.blocks.StructBlock([('Image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('Caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True))]))])))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
