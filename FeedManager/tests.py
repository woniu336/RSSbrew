from django.test import TestCase
from .models import OriginalFeed

# Create your tests here.

class OriginalFeedTests(TestCase):
    def test_single_url_no_title(self):
        """Test creating a single feed without title"""
        feed = OriginalFeed(url='http://example.com/feed1')
        feed.save()
        self.assertEqual(OriginalFeed.objects.count(), 1)
        self.assertEqual(feed.title, 'http://example.com/feed1')

    def test_single_url_with_title(self):
        """Test creating a single feed with title"""
        feed = OriginalFeed(url='http://example.com/feed1', title='Test Feed')
        feed.save()
        self.assertEqual(OriginalFeed.objects.count(), 1)
        self.assertEqual(feed.title, 'Test Feed')

    def test_multiple_urls_comma_separated(self):
        """Test creating multiple feeds with comma-separated URLs"""
        urls = 'http://example.com/feed1, http://example.com/feed2'
        feed = OriginalFeed(url=urls, title='Test Feed')
        feed.save()
        
        self.assertEqual(OriginalFeed.objects.count(), 2)
        feeds = OriginalFeed.objects.order_by('url')
        self.assertEqual(feeds[0].title, 'Test Feed-1')
        self.assertEqual(feeds[1].title, 'Test Feed-2')

    def test_multiple_urls_newline_separated(self):
        """Test creating multiple feeds with newline-separated URLs"""
        urls = '''http://example.com/feed1
        http://example.com/feed2'''
        feed = OriginalFeed(url=urls)
        feed.save()
        
        self.assertEqual(OriginalFeed.objects.count(), 2)
        feeds = OriginalFeed.objects.order_by('url')
        self.assertEqual(feeds[0].title, 'http://example.com/feed1')
        self.assertEqual(feeds[1].title, 'http://example.com/feed2')

    def test_mixed_separation_and_spacing(self):
        """Test creating multiple feeds with mixed separation and spacing"""
        urls = '''http://example.com/feed1,
        http://example.com/feed2 ,
           http://example.com/feed3'''
        feed = OriginalFeed(url=urls, title='Test Feed')
        feed.save()
        
        self.assertEqual(OriginalFeed.objects.count(), 3)
        feeds = OriginalFeed.objects.order_by('url')
        self.assertEqual(feeds[0].title, 'Test Feed-1')
        self.assertEqual(feeds[1].title, 'Test Feed-2')
        self.assertEqual(feeds[2].title, 'Test Feed-3')

    def test_duplicate_urls(self):
        """Test handling of duplicate URLs"""
        # First create a feed
        OriginalFeed.objects.create(url='http://example.com/feed1', title='Original')
        
        # Try to create the same feed in a batch
        urls = '''http://example.com/feed1,
        http://example.com/feed2'''
        feed = OriginalFeed(url=urls, title='Test Feed')
        feed.save()
        
        self.assertEqual(OriginalFeed.objects.count(), 2)
        # Original feed should keep its title
        original = OriginalFeed.objects.get(url='http://example.com/feed1')
        self.assertEqual(original.title, 'Original')
        # New feed should have the new title
        new_feed = OriginalFeed.objects.get(url='http://example.com/feed2')
        self.assertEqual(new_feed.title, 'Test Feed-1')
