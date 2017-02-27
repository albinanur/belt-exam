from django.shortcuts import render, redirect ,HttpResponse
from ..loginRegister.models import User
from .models import Item, Wishlist
from django.core.urlresolvers import reverse
from django.contrib import messages


def index(request):
	if not request.session['user_id']:
		return redirect(reverse('loginRegister:index'))

	othersWishList = Wishlist.objects.filter().exclude(user_id = request.session['user_id'])
	myWishlist = Wishlist.objects.filter(user_id = request.session['user_id'])
	excludeIdList = []
	for other in othersWishList:
		for my in myWishlist:
			if my.item.name == other.item.name:
				excludeIdList.append(other.id)
	context = {
		'myWishlist':Wishlist.objects.filter(user_id = request.session['user_id']),
		'othersWishList': Wishlist.objects.filter().exclude(user_id = request.session['user_id']).exclude(id__in=excludeIdList),
	}
	return render( request, 'wishList/index.html', context)

def create(request):

	return render(request, 'wishList/additem.html')

def add_new_wish(request):
	if (not request.POST['new_item'] or len(request.POST['new_item'])< 3):
		messages.warning(request, 'Please enter item or product with length more than 3!')
		return redirect(reverse('wishList:create'))
	else:
		user = User.objects.get(id = request.session['user_id'])
		item = Item.objects.create(name = request.POST['new_item'])
		Wishlist.objects.create(item=item, user=user, added_by = user.name)
		return redirect(reverse('wishList:index'))

def wish(request, id):
	context = {
		'item': Item.objects.get(id=id),
		'wish': Wishlist.objects.filter(item_id=id),
		'users': Wishlist.objects.filter(item_id=id),
	}
	return render( request, 'wishList/wish.html', context)

def add_to_my(request, id):
	user = User.objects.get(id=request.session['user_id'])
	wish = Wishlist.objects.get(item_id=id)
	item = Item.objects.get(id=id)
	Wishlist.objects.create(item=item, user=user, added_by=wish.user.name)

	return redirect(reverse('wishList:index'))

def delete(request, id):
	wish = Wishlist.objects.get(id=id)
	wish.delete()
	return redirect(reverse('wishList:index'))	

def remove(request, id):
	Wishlist.objects.get(id=id).delete()
	return redirect(reverse('wishList:index'))

