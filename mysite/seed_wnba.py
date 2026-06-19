from blog.models import Category, Post
cat, _ = Category.objects.get_or_create(name='Game Highlights', slug='game-highlights', description='Latest WNBA game recaps and highlights.')
cat2, _ = Category.objects.get_or_create(name='Player News', slug='player-news', description='Updates on your favorite WNBA players.')

Post.objects.get_or_create(
    title="A'ja Wilson Drops 30 Points in Stunning Aces Victory",
    slug="aja-wilson-30-points-aces-victory",
    defaults={
        'content': "Las Vegas Aces superstar A'ja Wilson put on an absolute clinic tonight, scoring 30 points and grabbing 15 rebounds to lead her team to a thrilling overtime victory. The two-time MVP showed exactly why she is considered one of the best players in the league...\n\nWilson's dominant performance in the paint was too much for the opposing defense. She was efficient from the floor and perfect from the free-throw line.",
        'category': cat,
        'status': 'published'
    }
)

Post.objects.get_or_create(
    title="Caitlin Clark Breaks Rookie Assist Record",
    slug="caitlin-clark-rookie-assist-record",
    defaults={
        'content': "Indiana Fever sensation Caitlin Clark has just shattered the WNBA rookie record for assists in a single season. With her court vision and incredible passing ability, Clark has transformed the Fever's offense into a fast-paced powerhouse.\n\nFans and analysts alike are marveling at her seamless transition from college basketball to the professional ranks.",
        'category': cat2,
        'status': 'published'
    }
)
