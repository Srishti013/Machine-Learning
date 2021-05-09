# Import the word cloud function  
from wordcloud import WordClloud

# Create and generate a word cloud image 
my_cloud = WordClloud(background_color='white', stopwords=my_stopwords).generate(descriptions)

# Display the generated wordcloud image
plt.imshow(my_cloud, interpolation='bilinear') 
plt.axis("off")

# Don't forget to show the final image
plt.show()