from django.shortcuts import render

def is_ajax(request):
  return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or request.META.get('HTTP_SEC_FETCH_MODE') == 'cors'

def ajax_required(f):
  def wrap(request, *args, **kwargs):
    if not is_ajax(request):
      return render(request, '400.html', status=400)
    return f(request, *args, **kwargs)
  wrap.__doc__=f.__doc__
  wrap.__name__=f.__name__
  return wrap