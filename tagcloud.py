import webbrowser
from wordfreq import wordfrequency
def generate_html_cloud():
	words = wordfrequency('./assignment')
	#~ min_font_size = 10
	#~ max_font_size = 50
	output = """<!DOCTYPE html><html><head><script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script></head><body><div style="width:80%; margin:10px auto;">"""
	for word in sorted(words):
		output += """<span data-ref="{}" style="font-size:{}px; display:inline-block; margin:10px 5px;" >{}</span>""".format(words[word][1], 10*words[word][0], word)
	output += """</div><div class="overlay" style="display:none;background-color:#000;opacity:0.5;width:100%;height:100%;position:fixed;left:0px;top:0px;z-index:1;"></div><div class="popup-content" style=" display:none;background-color:#fff;position:fixed;left:50%;top:50%;margin:-150px 0 0 -35%;padding:40px 10px 20px;text-align:center; width:70%;height:300px;z-index:2;"></div></body></html>
	<script>
	   jQuery('span').click(function(){
			var value = jQuery(this).attr('data-ref');
			jQuery('.overlay').show();
			jQuery('.popup-content').show();
			jQuery('.popup-content').html(value);
	   });
	   jQuery('.overlay,.popup-content').click(function(){
			jQuery('.overlay').hide();
			jQuery('.popup-content').hide();
	   });
	</script>"""
	f = open('./wordtagcloud.html','w')
	f.write(output)
	f.close()
	filename = './wordtagcloud.html'
	webbrowser.open_new_tab(filename)
if __name__ == "__main__":
	generate_html_cloud()	
