"""
An earlier version of the translation file was putting the lines into paragraphs. This became very unwieldy to edit, so I am unscrambling them here.
"""

import re
import json

text = """Pali: [0.1] Majjhima Nikāya 3 [0.2] Dhammadāyādasutta 

EN: [0.1] Middle Length Discourses 3 [0.2] Dhamma Heirs Discourse

Pali: [1.1] Evaṁ me sutaṁ—[1.2] ekaṁ samayaṁ bhagavā sāvatthiyaṁ viharati jetavane anāthapiṇḍikassa ārāme. [1.3] Tatra kho bhagavā bhikkhū āmantesi: [1.4] “bhikkhavo”ti. [1.5] “Bhadante”ti te bhikkhū bhagavato paccassosuṁ. [1.6] Bhagavā etadavoca: 

EN: [1.1] Thus have I heard.[1.2] At one time the Blessed One was staying near Savatthi in Jeta's Grove, Anathapindika's monastery. [1.3] There the Blessed One addressed the monks: [1.4] "Monks!" [1.5] "Venerable Sir," those monks replied to the Blessed One. [1.6] The Blessed One said this:

Pali: [2.1] “Dhammadāyādā me, bhikkhave, bhavatha, mā āmisadāyādā. [2.2] Atthi me tumhesu anukampā: [2.3] ‘kinti me sāvakā dhammadāyādā bhaveyyuṁ, no āmisadāyādā’ti. [2.4] Tumhe ca me, bhikkhave, āmisadāyādā bhaveyyātha no dhammadāyādā, tumhepi tena ādiyā bhaveyyātha: [2.5] ‘āmisadāyādā satthusāvakā viharanti, no dhammadāyādā’ti; [2.6] ahampi tena ādiyo bhaveyyaṁ: [2.7] ‘āmisadāyādā satthusāvakā viharanti, no dhammadāyādā’ti. 

EN: [2.1] "Be heirs of the Dhamma, monks, not heirs of material things. [2.2] There is compassion in me for you: [2.3] 'How might my disciples be heirs of the Dhamma, not heirs of material things?' [2.4] If you, monks, were to be heirs of material things and not heirs of the Dhamma, you would be liable to reproach: [2.5] 'The Teacher's disciples live as heirs of material things, not as heirs of the Dhamma'; [2.6] I too would be liable to reproach: [2.7] 'The Teacher's disciples live as heirs of material things, not as heirs of the Dhamma.'
EN-COMMENT: [2.4] "Ca me" is a Pali phrase where "ca" is a conjunction meaning "and" or "also," used for emphasis, and "me" is a dative pronoun meaning "to me" or "for me," but in this context signifies the Buddha's concern for his disciples. The Buddha uses this phrase to emphasize his instruction within the teacher-student dynamic, conveying both his authority and his benevolent concern for their spiritual progress.

Pali: [2.8] Tumhe ca me, bhikkhave, dhammadāyādā bhaveyyātha, no āmisadāyādā, tumhepi tena na ādiyā bhaveyyātha: [2.9] ‘dhammadāyādā satthusāvakā viharanti, no āmisadāyādā’ti; [2.10] ahampi tena na ādiyo bhaveyyaṁ: [2.11] ‘dhammadāyādā satthusāvakā viharanti, no āmisadāyādā’ti. [2.12] Tasmātiha me, bhikkhave, dhammadāyādā bhavatha, mā āmisadāyādā. [3.13] Atthi me tumhesu anukampā: [2.14] ‘kinti me sāvakā dhammadāyādā bhaveyyuṁ, no āmisadāyādā’ti. 
EN: [2.8] "And you, monks, should be heirs of the Dhamma, not heirs of material things. You too would not be liable to reproach: [2.9] 'The Teacher's disciples live as heirs of the Dhamma, not as heirs of material things'; [2.10] nor would I be liable to reproach: [2.11] 'The Teacher's disciples live as heirs of the Dhamma, not as heirs of material things.' [2.12] Therefore, monks, be heirs of the Dhamma, not heirs of material things. [2.13] There is compassion in me for you: [2.14] 'How might my disciples be heirs of the Dhamma, not heirs of material things?'"

Pali: [3.1] Idhāhaṁ, bhikkhave, bhuttāvī assaṁ pavārito paripuṇṇo pariyosito suhito yāvadattho; [3.2] siyā ca me piṇḍapāto atirekadhammo chaḍḍanīyadhammo. [3.3] Atha dve bhikkhū āgaccheyyuṁ jighacchādubbalyaparetā. [3.4] Tyāhaṁ evaṁ vadeyyaṁ: [3.5] ‘ahaṁ khomhi, bhikkhave, bhuttāvī pavārito paripuṇṇo pariyosito suhito yāvadattho; [3.6] atthi ca me ayaṁ piṇḍapāto atirekadhammo chaḍḍanīyadhammo. [3.7] Sace ākaṅkhatha, bhuñjatha, no ce tumhe bhuñjissatha, idānāhaṁ appaharite vā chaḍḍessāmi, appāṇake vā udake opilāpessāmī’ti. [3.8] Tatrekassa bhikkhuno evamassa: [3.9] ‘bhagavā kho bhuttāvī pavārito paripuṇṇo pariyosito suhito yāvadattho; [3.10] atthi cāyaṁ bhagavato piṇḍapāto atirekadhammo chaḍḍanīyadhammo. [3.11] Sace mayaṁ na bhuñjissāma, idāni bhagavā appaharite vā chaḍḍessati, appāṇake vā udake opilāpessati.
EN: [3.1] Here, monks, I suppose I have eaten, satisfied, full, done, content, and having had enough; [3.2] and there is my leftover alms-food that should be discarded. [3.3] Then two monks come, overcome by hunger and weakness. [3.4] Then I would say to them: [3.5] "Monks, I have eaten, satisfied, full, done, content, and having had enough; [3.6] and there is my leftover alms-food that should be discarded. [3.7] If you wish, eat it; if you do not eat it, I will now discard it in a barren place or pour it into water where no living beings dwell.' [3.8] Then one of the monks might think: [3.9] 'The Blessed One has eaten, is  satisfied, full, done, content, and having had enough; [3.10] and there is Blessed One's leftover alms-food that should be discarded. [3.11] If we do not eat it, the Blessed One will now discard it in a barren place or pour it into water where no living beings dwell.

Pali: [3.12] Vuttaṁ kho panetaṁ bhagavatā: [3.13] “dhammadāyādā me, bhikkhave, bhavatha, mā āmisadāyādā”ti. [3.14] Āmisaññataraṁ kho panetaṁ, yadidaṁ piṇḍapāto. [3.15] Yannūnāhaṁ imaṁ piṇḍapātaṁ abhuñjitvā imināva jighacchādubbalyena evaṁ imaṁ rattindivaṁ vītināmeyyan’ti. [3.16] So taṁ piṇḍapātaṁ abhuñjitvā teneva jighacchādubbalyena evaṁ taṁ rattindivaṁ vītināmeyya. [3.17] Atha dutiyassa bhikkhuno evamassa: [3.18] ‘bhagavā kho bhuttāvī pavārito paripuṇṇo pariyosito suhito yāvadattho; [3.19] atthi cāyaṁ bhagavato piṇḍapāto atirekadhammo chaḍḍanīyadhammo. [3.20] Sace mayaṁ na bhuñjissāma, idāni bhagavā appaharite vā chaḍḍessati, appāṇake vā udake opilāpessati. [3.21] Yannūnāhaṁ imaṁ piṇḍapātaṁ bhuñjitvā jighacchādubbalyaṁ paṭivinodetvā evaṁ imaṁ rattindivaṁ vītināmeyyan’ti. [3.22] So taṁ piṇḍapātaṁ bhuñjitvā jighacchādubbalyaṁ paṭivinodetvā evaṁ taṁ rattindivaṁ vītināmeyya. [3.23] Kiñcāpi so, bhikkhave, bhikkhu taṁ piṇḍapātaṁ bhuñjitvā jighacchādubbalyaṁ paṭivinodetvā evaṁ taṁ rattindivaṁ vītināmeyya, atha kho asuyeva me purimo bhikkhu pujjataro ca pāsaṁsataro ca. [3.24] Taṁ kissa hetu? [3.25] Tañhi tassa, bhikkhave, bhikkhuno dīgharattaṁ appicchatāya santuṭṭhiyā sallekhāya subharatāya vīriyārambhāya saṁvattissati. [3.26] Tasmātiha me, bhikkhave, dhammadāyādā bhavatha, mā āmisadāyādā. [3.27] Atthi me tumhesu anukampā: [3.28] ‘kinti me sāvakā dhammadāyādā bhaveyyuṁ, no āmisadāyādā’”ti. 

Pali: [4.1] Idamavoca bhagavā. [4.2] Idaṁ vatvāna sugato uṭṭhāyāsanā vihāraṁ pāvisi. [4.3] Tatra kho āyasmā sāriputto acirapakkantassa bhagavato bhikkhū āmantesi: [4.4] “āvuso bhikkhave”ti. [4.5] “Āvuso”ti kho te bhikkhū āyasmato sāriputtassa paccassosuṁ. [4.6] Āyasmā sāriputto etadavoca: 

Pali: [5.1] “Kittāvatā nu kho, āvuso, satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhanti, kittāvatā ca pana satthu pavivittassa viharato sāvakā vivekamanusikkhantī”ti? [5.2] “Dūratopi kho mayaṁ, āvuso, āgacchāma āyasmato sāriputtassa santike etassa bhāsitassa atthamaññātuṁ. [5.3] Sādhu vatāyasmantaṁyeva sāriputtaṁ paṭibhātu etassa bhāsitassa attho; [5.4] āyasmato sāriputtassa sutvā bhikkhū dhāressantī”ti. [5.5] “Tena hāvuso, suṇātha, sādhukaṁ manasi karotha, bhāsissāmī”ti. [5.6] “Evamāvuso”ti kho te bhikkhū āyasmato sāriputtassa paccassosuṁ. [5.7] Āyasmā sāriputto etadavoca: 

Pali: [6.1] “Kittāvatā nu kho, āvuso, satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhanti? [6.2] Idhāvuso, satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhanti, [6.3] yesañca dhammānaṁ satthā pahānamāha, te ca dhamme nappajahanti, [6.4] bāhulikā ca honti, sāthalikā, okkamane pubbaṅgamā, paviveke nikkhittadhurā. [6.5] Tatrāvuso, therā bhikkhū tīhi ṭhānehi gārayhā bhavanti. [6.6] ‘Satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhantī’ti—[6.7] iminā paṭhamena ṭhānena therā bhikkhū gārayhā bhavanti. [6.8] ‘Yesañca dhammānaṁ satthā pahānamāha te ca dhamme nappajahantī’ti—[6.9] iminā dutiyena ṭhānena therā bhikkhū gārayhā bhavanti. [6.10] ‘Bāhulikā ca, sāthalikā, okkamane pubbaṅgamā, paviveke nikkhittadhurā’ti—[6.11] iminā tatiyena ṭhānena therā bhikkhū gārayhā bhavanti. [6.12] Therā, āvuso, bhikkhū imehi tīhi ṭhānehi gārayhā bhavanti. [6.13] Tatrāvuso, majjhimā bhikkhū …pe… [6.14] navā bhikkhū tīhi ṭhānehi gārayhā bhavanti. [6.15] ‘Satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhantī’ti—[6.16] iminā paṭhamena ṭhānena navā bhikkhū gārayhā bhavanti. [6.17] ‘Yesañca dhammānaṁ satthā pahānamāha te ca dhamme nappajahantī’ti—[6.18] iminā dutiyena ṭhānena navā bhikkhū gārayhā bhavanti. [6.19] ‘Bāhulikā ca honti, sāthalikā, okkamane pubbaṅgamā, paviveke nikkhittadhurā’ti—[6.20] iminā tatiyena ṭhānena navā bhikkhū gārayhā bhavanti. [6.21] Navā, āvuso, bhikkhū imehi tīhi ṭhānehi gārayhā bhavanti. [6.22] Ettāvatā kho, āvuso, satthu pavivittassa viharato sāvakā vivekaṁ nānusikkhanti. 

Pali: [7.1] Kittāvatā ca panāvuso, satthu pavivittassa viharato sāvakā vivekamanusikkhanti? [7.2] Idhāvuso, satthu pavivittassa viharato sāvakā vivekamanusikkhanti—[7.3] yesañca dhammānaṁ satthā pahānamāha te ca dhamme pajahanti; [7.4] na ca bāhulikā honti, na sāthalikā okkamane nikkhittadhurā paviveke pubbaṅgamā. [7.5] Tatrāvuso, therā bhikkhū tīhi ṭhānehi pāsaṁsā bhavanti. [7.6] ‘Satthu pavivittassa viharato sāvakā vivekamanusikkhantī’ti—[7.7] iminā paṭhamena ṭhānena therā bhikkhū pāsaṁsā bhavanti. [7.8] ‘Yesañca dhammānaṁ satthā pahānamāha te ca dhamme pajahantī’ti—[7.9] iminā dutiyena ṭhānena therā bhikkhū pāsaṁsā bhavanti. [7.10] ‘Na ca bāhulikā, na sāthalikā okkamane nikkhittadhurā paviveke pubbaṅgamā’ti—[7.11] iminā tatiyena ṭhānena therā bhikkhū pāsaṁsā bhavanti. [7.12] Therā, āvuso, bhikkhū imehi tīhi ṭhānehi pāsaṁsā bhavanti. [7.13] Tatrāvuso, majjhimā bhikkhū …pe… [7.14] navā bhikkhū tīhi ṭhānehi pāsaṁsā bhavanti. [7.15] ‘Satthu pavivittassa viharato sāvakā vivekamanusikkhantī’ti—[7.16] iminā paṭhamena ṭhānena navā bhikkhū pāsaṁsā bhavanti. [7.17] ‘Yesañca dhammānaṁ satthā pahānamāha te ca dhamme pajahantī’ti—[7.18] iminā dutiyena ṭhānena navā bhikkhū pāsaṁsā bhavanti. [7.19] ‘Na ca bāhulikā, na sāthalikā okkamane nikkhittadhurā paviveke pubbaṅgamā’ti—[7.20] iminā tatiyena ṭhānena navā bhikkhū pāsaṁsā bhavanti. [7.21] Navā, āvuso, bhikkhū imehi tīhi ṭhānehi pāsaṁsā bhavanti. [7.22] Ettāvatā kho, āvuso, satthu pavivittassa viharato sāvakā vivekamanusikkhanti.

Pali: [8.1] Tatrāvuso, lobho ca pāpako doso ca pāpako. [8.2] Lobhassa ca pahānāya dosassa ca pahānāya atthi majjhimā paṭipadā cakkhukaraṇī ñāṇakaraṇī upasamāya abhiññāya sambodhāya nibbānāya saṁvattati. [8.3] Katamā ca sā, āvuso, majjhimā paṭipadā cakkhukaraṇī ñāṇakaraṇī upasamāya abhiññāya sambodhāya nibbānāya saṁvattati? [8.4] Ayameva ariyo aṭṭhaṅgiko maggo, seyyathidaṁ—[8.5] sammādiṭṭhi sammāsaṅkappo sammāvācā sammākammanto sammāājīvo sammāvāyāmo sammāsati sammāsamādhi. [8.6] Ayaṁ kho sā, āvuso, majjhimā paṭipadā cakkhukaraṇī ñāṇakaraṇī upasamāya abhiññāya sambodhāya nibbānāya saṁvattati."""

en_segments_dict = {}
for en_line in filter(lambda x: x.startswith("EN: "), text.splitlines()):
    line = en_line[len("EN: ") :]

    matches = re.findall(r"\[(\d+\.\d+)\](.*?)(?=\[\d+\.\d+\]|$)", line)

    en_segments_dict.update({segment: text[1:] for segment, text in matches})

en_comment_dict = {}
for en_comment_line in filter(
    lambda x: x.startswith("EN-COMMENT: "), text.splitlines()
):
    line = en_comment_line[len("EN-COMMENT: ") :]

    matches = re.findall(r"\[(\d+\.\d+)\](.*?)(?=\[\d+\.\d+\]|$)", line)

    en_comment_dict.update({segment: text[1:] for segment, text in matches})

with open(
    "suttas/root/mn/mn3_root-pli-ms.json", "r", encoding="utf-8"
) as f:  # Open the file in read mode with UTF-8 encoding
    pali_segments_dict = json.load(f)
    pali_segments_dict = {
        key[len("mn3:") :]: value for key, value in pali_segments_dict.items()
    }

output = ""
for pali_segment, pali_line in pali_segments_dict.items():
    output += f"Pali [{pali_segment}]: {pali_line}\n"
    if pali_segment in en_segments_dict:
        output += f"EN [{pali_segment}]: {en_segments_dict[pali_segment]}\n"
    if pali_segment in en_comment_dict:
        output += f"EN-COMMENT [{pali_segment}: {en_comment_dict[pali_segment]}\n"
    output += "\n"
print(output)
    
