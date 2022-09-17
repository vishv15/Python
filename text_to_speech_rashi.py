import gtts
from playsound import playsound
#make request to google to get synthesis
line="""પોઝિટિવઃ- છેલ્લી થોડી ભૂલોથી બોધપાઠ લઇને તમે તમારી કાર્યપ્રણાલીમાં થોડો પરિવર્તન લાવશો, જે સારો સાબિત થશે.
 કોઇ નજીકના સંબંધી સાથે ચાલી રહેલો વિવાદ પણ ઉકેલાઇ શકે છે.
 યુવાઓને કરિયરને લગતી કોઇ પરીક્ષામાં સફળતા મળવાની શક્યતા છે."""

tts=gtts.gTTS(line,lang="gu")
tts.save("hello1.mp3")
playsound("hello1.mp3")
print("done...")