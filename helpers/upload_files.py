def upload_product_image(instance, filename):
    return f"{instance.name}/{filename}"
