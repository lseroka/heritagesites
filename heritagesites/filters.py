import django_filters
from heritagesites.models import CountryArea, HeritageSite, HeritageSiteCategory, \
	IntermediateRegion, SubRegion, Region


class HeritageSiteFilter(django_filters.FilterSet):
	site_name = django_filters.CharFilter(
		field_name='site_name',
		label='Heritage Site Name',
		lookup_expr='icontains'
	)

	description = django_filters.CharFilter(
		field_name='description',
		label='Heritage Site Description',
		lookup_expr='icontains'
	) 

	category = django_filters.ModelChoiceFilter(
		field_name='heritage_site__heritage_site_category__category_name',
		label = 'Heritage Site Category',
		query_set = HeritageSiteCategory.objects.all().order_by('heritage_site_category__category_name'),
		lookup_expr='exact'
	)

	region = django_filters.ModelChoiceFilter(
		field_name='country_area__location__region__region_name',
		label = 'Region',
		query_set = Region.objects.all().order_by('region__region_name'),
		lookup_expr='exact'
	)

	sub_region = django_filters.ModelChoiceFilter(
		field_name='country_area__location__sub_region__sub_region_name',
		label = 'SubRegion',
		query_set = SubRegion.objects.all().order_by('sub_region__sub_region_name'),
		lookup_expr='exact'
	)

	intermediate_region = django_filters.ModelChoiceFilter(
		field_name='country_area__location__intermediate_region__intermediate_region_name',
		label = 'IntermediateRegion',
		query_set = IntermediateRegion.objects.all().order_by('intermediate_region__intermediate_region_name'),
		lookup_expr='exact'
	)

	country_area = django_filters.ModelChoiceFilter(
		field_name='country_area',
		label='Country/Area',
		queryset=CountryArea.objects.all().order_by('country_area_name'),
		lookup_expr='exact'
	)

	date_inscribed = django_filters.NumberFilter(
		field_name = 'date_inscribed',
		label = 'Date Inscribed',
		lookup_expr = 'exact'
	)



	class Meta:
		model = HeritageSite
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []






