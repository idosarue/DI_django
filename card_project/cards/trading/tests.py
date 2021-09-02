from django.test import TestCase

# Create your tests here.
# <QuerySet [<Card: Luke Skywalker>, <Card: R2-D2>, <Card: Darth 
# Vader>, <Card: Owen Lars>, <Card: Beru Whitesun lars>, <Card: Obi-Wan Kenobi>, <Card: T-16 skyhopper>, <Card: X-34 landspeeder>, <Card: Snowspeeder>, <Card: TIE bomber>, <Card: Sail barge>, <Card: C-3PO>, <Card: Leia Organa>]> before1
# <QuerySet [<Card: Luke Skywalker>, <Card: C-3PO>, <Card: Beru Whitesun lars>, <Card: Obi-Wan Kenobi>, <Card: Sand Crawler>, <Card: T-16 skyhopper>, <Card: X-34 landspeeder>, <Card: TIE/LN starfighter>, <Card: TIE bomber>, <Card: Sail barge>, <Card: Snowspeeder>, <Card: Darth Vader>]> before2
# <QuerySet [<Card: Luke Skywalker>, <Card: R2-D2>, <Card: Darth 
# Vader>, <Card: Owen Lars>, <Card: Beru Whitesun lars>, <Card: Obi-Wan Kenobi>, <Card: T-16 skyhopper>, <Card: X-34 landspeeder>, <Card: Snowspeeder>, <Card: TIE bomber>, <Card: Sail barge>, <Card: C-3PO>, <Card: Leia Organa>]> after1
# <QuerySet [<Card: Luke Skywalker>, <Card: C-3PO>, <Card: Beru Whitesun lars>, <Card: Obi-Wan Kenobi>, <Card: T-16 skyhopper>, <Card: X-34 landspeeder>, <Card: TIE/LN starfighter>, <Card: TIE bomber>, <Card: Sail barge>, <Card: Snowspeeder>, <Card: Darth Vader>, <Card: Leia Organa>]> after2