# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html dir="ltr" lang="en-US">
<head>

	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="author" content="FernandoBalmaceda" />

	<!-- Stylesheets
	============================================= -->
	<link href="http://fonts.googleapis.com/css?family=Mukta+Vaani:300,400,500,600,700|Open+Sans:300,400,600,700,800,900" rel="stylesheet" type="text/css" />
	<link rel="stylesheet" href="view/css/bootstrap.css" type="text/css" />
	<link rel="stylesheet" href="view/style.css" type="text/css" />
	<link rel="stylesheet" href="view/css/dark.css" type="text/css" />
	<link rel="stylesheet" href="view/css/swiper.css" type="text/css" />

	<!-- Bootstrap Select CSS -->
	<link rel="stylesheet" href="view/css/components/bs-select.css" type="text/css" />

	<!-- car Specific Stylesheet -->
	<link rel="stylesheet" href="view/demos/car/car.css" type="text/css" />
	<link rel="stylesheet" href="view/demos/car/css/car-icons/style.css" type="text/css" />
	<!-- / -->

	<link rel="stylesheet" href="view/css/font-icons.css" type="text/css" />
	<link rel="stylesheet" href="view/css/animate.css" type="text/css" />
	<link rel="stylesheet" href="view/css/magnific-popup.css" type="text/css" />

	<link rel="stylesheet" href="view/demos/car/css/fonts.css" type="text/css" />

	<link rel="stylesheet" href="view/css/responsive.css" type="text/css" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<!--[if lt IE 9]>
		<script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script>
	<![endif]-->

	<!-- Document Title
	============================================= -->
	<title>Fernando Balmaceda | Movie Website Project</title>

	<style>
		/* Revolution Slider */
		.ares .tp-tab { border: 1px solid #eee; }
		.ares .tp-tab-content { margin-top: -4px; }
		.ares .tp-tab-content { padding: 15px 15px 15px 110px; }
		.ares .tp-tab-image { width: 80px;height: 80px; }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
	</style>

</head>
'''


# The main page layout and title bar
main_page_content = '''
<body class="stretched side-push-panel" data-loader-html="<div><img src='view/demos/car/images/page-loader.gif' alt='Loader'></div>">

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
	<!-- Side Panel Overlay -->
	<div class="body-overlay"></div>

	<!-- Document Wrapper
	============================================= -->
	<div id="wrapper" class="clearfix">

		<!-- Header
		============================================= -->
		<header id="header" class="static-sticky full-header clearfix">

			<div id="header-wrap">

				<div class="container-fluid clearfix">

					<div id="primary-menu-trigger"><i class="icon-reorder"></i></div>

					<!-- Primary Navigation
					============================================= -->
					<nav id="primary-menu" class="with-arrows clearfix">
						<ul>
							<li class="current"><a href="#"><div>WEBSITE MOVIE TRAILERS</div></a></li>
						</ul>
					</nav><!-- #primary-menu end -->
				</div>

			</div>

			<div id="header-trigger"><i class="icon-line-menu"></i><i class="icon-line-cross"></i></div>

		</header><!-- #header end -->

		<!-- Slider
		============================================= -->
		<section id="slider" class="slider-element swiper_wrapper full-screen clearfix" data-dots="true" data-loop="true" data-grab="false">

			<div class="swiper-container swiper-parent">
				<div class="swiper-wrapper">
					{movie_tiles}
				</div>
				<div class="swiper-pagination"></div>
			</div>

		</section>
	</div><!-- #wrapper end -->

	<!-- External JavaScripts
	============================================= -->
	<script src="view/js/jquery.js"></script>
	<script src="view/js/plugins.js"></script>

	<!-- Footer Scripts
	============================================= -->
	<script src="view/js/functions.js"></script>
	<script src="view/js/movie_website.js"></script>
</body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="swiper-slide dark" style="background-image: url('{poster_image_url}'); background-size: cover">
    <div class="container clearfix">
        <div class="slider-caption top-left center">
            <h2 class="font-primary nott">{movie_title}</h2>
            <p class="t300 font-primary d-none d-sm-block">{movie_short_description}</p>
            <a href="#" id="movie_triler_video" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" class="button button-rounded button-border button-white button-light nott">View Trailer</a>
        </div>
    </div>
</div>
'''