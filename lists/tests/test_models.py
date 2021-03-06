from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

class ListAndItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())
    
    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')

        ''' 
        # as opposed to doing something like this:
        try :
            item.save()
            self.fail('the save should have raised an exception)
        except ValidationError:
            pass

        # we can use Python's built in context manager, With, to wrap the code and make it a bit more readable. 
        '''
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean() # not quite able to get my head around this one, see page 220. something to do with how Django does data validation? V0od0o!!1

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list_, text='bla')
            item.full_clean()

    def test_can_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() # should not raise
    
    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')

        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )        

    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')

class ListModelTest(TestCase):
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

    def test_create_new_creates_list_and_first_item(self):
        List.create_new(first_item_text='new item text')
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'new item text')
        new_list = List.objects.first()
        self.assertEqual(new_item.list, new_list)

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()
        List.create_new(first_item_text='new item text', owner=user)
        new_list = List.objects.first()
        self.assertEqual(new_list.owner, user)

    def test_lists_can_have_owners(self):
        List(owner=User()) # should not raise

    def test_list_owner_is_optional(self):
        List().full_clean() # should not raise

    def test_create_returns_new_list_objects(self):
        returned = List.create_new(first_item_text='new item text')
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)

    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='first item')
        Item.objects.create(list=list_, text='second item')
        self.assertEqual(list_.name, 'first item')
    
    def test_list_shared_with_add_method(self):
        list_ = List.objects.create()
        sharee = User.objects.create(email='share@bc.com')
        list_.shared_with.add(sharee)
        self.assertIn(sharee, list_.shared_with.all())

    def test_shared_with_add_functionality(self):
        new_user_email_one = 'ben_jacobson@live.com'
        new_user_email_two = 'user@example.com'

        # Create the users
        user_one = User.objects.create(email=new_user_email_one)
        user_two = User.objects.create(email=new_user_email_two)

        # create two lists
        list_one = List.create_new(first_item_text="list_one", owner=user_one)
        list_two = List.create_new(first_item_text="list_two", owner=user_two)

        # test that the users have been created
        self.assertEqual(list_one.owner.email, new_user_email_one)
        self.assertEqual(list_two.owner.email, new_user_email_two)

        # attempt to link the two by sharing one list with the other
        list_one.shared_with.add(user_two)

        # prove that it worked:
        shared_with_email_test = list_one.shared_with.all().first().email
        self.assertEqual(shared_with_email_test, new_user_email_two)

        # Since the 'My lists' page relies on list ownership, check that ownership is correct also
        

