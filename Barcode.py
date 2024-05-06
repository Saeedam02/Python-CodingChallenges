import barcode
from barcode.writer import ImageWriter

barcode_format = barcode.get_barcode_class(
    'code128'
)
data = '123456789'
my_barcode = barcode_format(
    data, writer = ImageWriter()
)

my_barcode.save('my_barcode')
print(my_barcode.render())