from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/project/')
    link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']  


class QuotationRequest(models.Model):
    # Project Category Choices
    WEBSITE_DEVELOPMENT = 'Website Development'
    ECOMMERCE_SITE = 'E-commerce Site'
    WEB_APPLICATION = 'Web Application'
    UIUX_DESIGN = 'UI/UX Design'
    LANDING_PAGE_DESIGN = 'Landing Page Design'

    PROJECT_CATEGORY_CHOICES = [
        (WEBSITE_DEVELOPMENT, 'Website Development'),
        (ECOMMERCE_SITE, 'E-commerce Site'),
        (WEB_APPLICATION, 'Web Application'),
        (UIUX_DESIGN, 'UI/UX Design'),
        (LANDING_PAGE_DESIGN, 'Landing Page Design'),
    ]

    # Budget Range Choices
    BUDGET_10K_25K = 'KES 10,000 - KES 25,000'
    BUDGET_25K_50K = 'KES 25,000 - KES 50,000'
    BUDGET_50K_100K = 'KES 50,000 - KES 100,000'
    BUDGET_100K_PLUS = 'KES 100,000+'

    BUDGET_RANGE_CHOICES = [
        (BUDGET_10K_25K, 'KES 10,000 - KES 25,000'),
        (BUDGET_25K_50K, 'KES 25,000 - KES 50,000'),
        (BUDGET_50K_100K, 'KES 50,000 - KES 100,000'),
        (BUDGET_100K_PLUS, 'KES 100,000+'),
    ]

    # Model Fields
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    project_category = models.CharField(
        max_length=50,
        choices=PROJECT_CATEGORY_CHOICES,
    )
    budget_range = models.CharField(
        max_length=50,
        choices=BUDGET_RANGE_CHOICES,
    )
    project_description = models.TextField()
    timeline = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name