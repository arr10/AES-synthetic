ANONYMIZATION = """
Anonymization
All the essays are anonymized. This means that the named entities (people, places, dates,
times, organizations, etc.) are replaced by placeholders (Eg. @NAME1, @LOCATION1, etc.). In
addition to this, capitalized phrases are anonymized as @CAPS1, @CAPS2, etc. These
anonymizations should not affect your scoring.
                """

CONTENT_RUBURIC = """
Content
This property checks for the amount of content and ideas present in the essay.

Score 6: The writing is exceptionally clear, focused, and interesting. It holds the reader’s attention throughout.
Main ideas stand out and are developed by strong support and rich details suitable to audience and purpose. 
The writing is characterized by
• clarity, focus, and control.
• main idea(s) that stand out.
• supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
• a thorough, balanced, in-depth explanation / exploration of the topic; the writing makes connections and shares insights.
• content and selected details that are well-suited to audience and purpose.

Score 5: The writing is clear, focused and interesting. It holds the reader’s attention. Main ideas
stand out and are developed by supporting details suitable to audience and purpose. The
writing is characterized by
• clarity, focus, and control.
• main idea(s) that stand out.
• supporting, relevant, carefully selected details; when appropriate, use of resources provides strong, accurate, credible support.
• a thorough, balanced explanation / exploration of the topic; the writing makes connections and shares insights.
• content and selected details that are well-suited to audience and purpose.

Score 4: The writing is clear and focused. The reader can easily understand the main ideas.
Support is present, although it may be limited or rather general. The writing is characterized by
• an easily identifiable purpose.
• clear main idea(s).
• supporting details that are relevant, but may be overly general or limited in places; when appropriate, resources are used to provide accurate support.
• a topic that is explored / explained, although developmental details may occasionally be out of balance with the main idea(s); some connections and insights may be present.
• content and selected details that are relevant, but perhaps not consistently well-chosen for audience and purpose.

Score 3: The reader can understand the main ideas, although they may be overly broad or simplistic, and the results may not be effective. Supporting detail is often limited, insubstantial, overly general, or occasionally slightly off-topic. The writing is characterized by
• an easily identifiable purpose and main idea(s).
• predictable or overly-obvious main ideas; or points that echo observations heard elsewhere; or a close retelling of another work.
• support that is attempted, but developmental details are often limited, uneven, somewhat off-topic, predictable, or too general (e.g., a list of underdeveloped points).
• details that may not be well-grounded in credible resources; they may be based on clichés, stereotypes or questionable sources of information.
• difficulties when moving from general observations to specifics.

Score 2: Main ideas and purpose are somewhat unclear or development is attempted but minimal. The writing is characterized by
• a purpose and main idea(s) that may require extensive inferences by the reader.
• minimal development; insufficient details.
• irrelevant details that clutter the text.
• extensive repetition of detail.

Score 1: The writing lacks a central idea or purpose. The writing is characterized by
• ideas that are extremely limited or simply unclear.
• attempts at development that are minimal or nonexistent; the paper is too short to demonstrate the development of an idea.
"""

CONTENT_RUBURIC_2 = """
Content

Score 4: The response answers the question asked of it. 
Supporting evidence is specific to the memoir is used to support the points the writer makes..

Score 3: The response mostly answers the question asked of it. 
Sufficient evidence from the memoir is used to support the points that the writer makes.

Score 2: The response addresses some of the points. 
Evidence from the story supporting those points are present.

Score 1: The response is minimal to answering the question. 
It uses little / no information from the memoir and may include misrepresentations.

Score 0: The response is irrelevant / incorrect / incomplete.
"""

CONTENT_RUBURIC_3 = """
Content
Score 3: The response answers the question asked of it. Sufficient evidence from the story is used to support the points that the writer makes.
Score 2: The response addresses some of the points. Evidence from the story supporting those points are present.
Score 1: The response may lack information / evidence showing a lack of understanding of the text.
Score 0: The response is irrelevant / incorrect / incomplete.
"""

CONTENT_RUBURIC_4 = """
Content
Score 3: Tells a story with ideas that are clearly focused on the topic and are thoroughly developed with
specific, relevant details.
Score 2: Tells a story with ideas that are somewhat focused on the topic and are developed with a mix of
specific and/or general details.
Score 1: Tells a story with ideas that are minimally focused on the topic and developed with limited
and/or general details.
Score 0: Ideas are not focused on the task and/or are undeveloped.
"""


ORGANIZATION_RUBURIC = """
Organization

This property checks how well structured the essay is. NOTE: Since the dataset has the essays compressed into one line, please bear in mind that the paragraph information is lost. Hence, give writers the benefit of the doubt here.

Score 6: The essay is well-organized. There is a clear flow of ideas with each idea self-contained (this is where we assume that each idea is contained in a paragraph). The essay has the appropriate form as a letter to the editor.

Score 5: The essay shows good organization. There is a flow of ideas. However, the ideas are mostly self-contained. The essay has the appropriate form as a letter to the editor.

Score 4: The essay shows satisfactory organization. It contains a basic introduction, body and conclusion.

Score 3: The essay shows some organization. Its form may not be that of a letter to the editor. Its ideas are not necessarily self-contained.

Score 2: Shows little or no evidence of organization.

Score 1: The essay is awkward and fragmented. Ideas are not self-contained.
"""

ORGANIZATION_RUBURIC_2 = """
Organization

Score 3: Organization and connections between ideas and/or events are clear and logically sequenced.
Score 2: Organization and connections between ideas and/or events are logically sequenced.
Score 1: Organization and connections between ideas and/or events are weak.
Score 0: No organization evident.
"""

ORGANIZATION_RUBURIC_3 = """
Organization

Score 6: The organization enhances the central idea(s) and its development. 
The order and structure are compelling and move the reader through the text easily. 
The writing is characterized by
• effective, perhaps creative, sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
• a strong, inviting beginning that draws the reader in and a strong, satisfying sense of resolution or closure.
• smooth, effective transitions among all elements (sentences, paragraphs, ideas).
• details that fit where placed.

Score 5: The organization enhances the central idea(s) and its development. 
The order and structure are strong and move the reader through the text. The writing is characterized by
• effective sequencing and paragraph breaks; the organizational structure fits the topic, and the writing is easy to follow.
• an inviting beginning that draws the reader in and a satisfying sense of resolution or closure.
• smooth, effective transitions among all elements (sentences, paragraphs, ideas).
• details that fit where placed.

Score 4: Organization is clear and coherent. Order and structure are present, but may seem formulaic.
The writing is characterized by
• clear sequencing and paragraph breaks.
• an organization that may be predictable.
• a recognizable, developed beginning that may not be particularly inviting; a developed conclusion that may lack subtlety.
• a body that is easy to follow with details that fit where placed.
• transitions that may be stilted or formulaic.
• organization which helps the reader, despite some weaknesses.

Score 3: An attempt has been made to organize the writing; however, the overall structure is inconsistent or skeletal. 
The writing is characterized by
• attempts at sequencing and paragraph breaks, but the order or the relationship among ideas may occasionally be unclear.
• a beginning and an ending which, although present, are either undeveloped or too obvious (e.g., “My topic is...”; “These are all the reasons that...”).
• transitions that sometimes work. The same few transitional devices (e.g., coordinating conjunctions, numbering, etc.) may be overused.
• a structure that is skeletal or too rigid.
• placement of details that may not always be effective.
• organization which lapses in some places, but helps the reader in others.

Score 2: The writing lacks a clear organizational structure. An occasional organizational device is discernible; however, the writing is either difficult to follow and the reader has to reread substantial
portions, or the piece is simply too short to demonstrate organizational skills. The writing is characterized by
• some attempts at sequencing, but the order or the relationship among ideas is frequently unclear; a lack of paragraph breaks.
• a missing or extremely undeveloped beginning, body, and/or ending.
• a lack of transitions, or when present, ineffective or overused.
• a lack of an effective organizational structure.
• details that seem to be randomly placed, leaving the reader frequently confused.

Score 1: The writing lacks coherence; organization seems haphazard and disjointed. Even after rereading, the reader remains confused. The writing is characterized by
• a lack of effective sequencing and paragraph breaks.
• a failure to provide an identifiable beginning, body and/or ending.
• a lack of transitions.
• pacing that is consistently awkward; the reader feels either mired down in trivia or rushed along too rapidly.
• a lack of organization which ultimately obscures or distorts the main point.
"""


WORD_CHOICE_RUBURIC = """
Word Choice

Score 6: Words convey the intended message in an exceptionally interesting, precise, and natural way appropriate to audience and purpose. 
The writer employs a rich, broad range of words which have been carefully chosen and thoughtfully placed for impact. 
The writing is characterized by
• accurate, strong, specific words; powerful words energize the writing.
• fresh, original expression; slang, if used, seems purposeful and is effective.
• vocabulary that is striking and varied, but that is natural and not overdone.
• ordinary words used in an unusual way.
• words that evoke strong images; figurative language may be used.

Score 5: Words convey the intended message in an interesting, precise, and natural way appropriate to audience and purpose. 
The writer employs a broad range of words which have been carefully chosen and thoughtfully placed for impact. 
The writing is characterized by
• accurate, specific words; word choices energize the writing.
• fresh, vivid expression; slang, if used, seems purposeful and is effective.
• vocabulary that may be striking and varied, but that is natural and not overdone.
• ordinary words used in an unusual way.
• words that evoke clear images; figurative language may be used.

Score 4: Words effectively convey the intended message. 
The writer employs a variety of words that are functional and appropriate to audience and purpose. 
The writing is characterized by
• words that work but do not particularly energize the writing.
• expression that is functional; however, slang, if used, does not seem purposeful and is not particularly effective.
• attempts at colorful language that may occasionally seem overdone.
• occasional overuse of technical language or jargon.
• rare experiments with language; however, the writing may have some fine moments and generally avoids clichés.

Score 3: Language lacks precision and variety, or may be inappropriate to audience and purpose in places. 
The writer does not employ a variety of words, producing a sort of “generic”
paper filled with familiar words and phrases. The writing is characterized by
• words that work, but that rarely capture the reader’s interest.
• expression that seems mundane and general; slang, if used, does not seem purposeful and is not effective.
• attempts at colorful language that seem overdone or forced.
• words that are accurate for the most part, although misused words may occasionally appear; technical language or jargon may be overused or inappropriately used.
• reliance on clichés and overused expressions.
• text that is too short to demonstrate variety.

Score 2: Language is monotonous and/or misused, detracting from the meaning and impact. 
The writing is characterized by
• words that are colorless, flat or imprecise.
• monotonous repetition or overwhelming reliance on worn expressions that repeatedly detract from the message.

Score 1: The writing shows an extremely limited vocabulary or is so filled with misuses of words that the meaning is obscured. 
Only the most general kind of message is communicated because of vague or imprecise language. The writing is characterized by
• general, vague words that fail to communicate.
• an extremely limited range of words.
• words that simply do not fit the text; they seem imprecise, inadequate, or just plain wrong.
"""

SENTENCE_FLUENCY_RUBURIC = """
Sentence Fluency

Score 6: The writing has an effective flow and rhythm. 
Sentences show a high degree of craftsmanship, with consistently strong and varied structure that makes expressive oral reading easy and enjoyable. 
The writing is characterized by
• a natural, fluent sound; it glides along with one sentence flowing effortlessly into the next.
• extensive variation in sentence structure, length, and beginnings that add interest to the text.
• sentence structure that enhances meaning by drawing attention to key ideas or reinforcing relationships among ideas.
• varied sentence patterns that create an effective combination of power and grace.
• strong control over sentence structure; fragments, if used at all, work well.
• stylistic control; dialogue, if used, sounds natural.

Score 5: The writing has an easy flow and rhythm. 
Sentences are carefully crafted, with strong and varied structure that makes expressive oral reading easy and enjoyable. 
The writing is characterized by
• a natural, fluent sound; it glides along with one sentence flowing into the next.
• variation in sentence structure, length, and beginnings that add interest to the text.
• sentence structure that enhances meaning.
• control over sentence structure; fragments, if used at all, work well.
• stylistic control; dialogue, if used, sounds natural.

Score 4: The writing flows; however, connections between phrases or sentences may be less than fluid. 
Sentence patterns are somewhat varied, contributing to ease in oral reading. 
The writing is characterized by
• a natural sound; the reader can move easily through the piece, although it may lack a certain rhythm and grace.
• some repeated patterns of sentence structure, length, and beginnings that may detract somewhat from overall impact.
• strong control over simple sentence structures, but variable control over more complex sentences; fragments, if present, are usually effective.
• occasional lapses in stylistic control; dialogue, if used, sounds natural for the most part, but may at times sound stilted or unnatural.

Score 3: The writing tends to be mechanical rather than fluid. 
Occasional awkward constructions may force the reader to slow down or reread. 
The writing is characterized by
• some passages that invite fluid oral reading; however, others do not.
• some variety in sentence structure, length, and beginnings, although the writer falls into repetitive sentence patterns.
• good control over simple sentence structures, but little control over more complex sentences; fragments, if present, may not be effective.
• sentences which, although functional, lack energy.
• lapses in stylistic control; dialogue, if used, may sound stilted or unnatural.
• text that is too short to demonstrate variety and control.

Score 2: The writing tends to be either choppy or rambling. 
Awkward constructions often force the reader to slow down or reread. The writing is characterized by
• significant portions of the text that are difficult to follow or read aloud.
• sentence patterns that are monotonous (e.g., subject-verb or subject-verb-object).
• a significant number of awkward, choppy, or rambling constructions.

Score 1: The writing is difficult to follow or to read aloud. 
Sentences tend to be incomplete, rambling, or very awkward. 
The writing is characterized by
• text that does not invite—and may not even permit—smooth oral reading.
• confusing word order that is often jarring and irregular.
• sentence structure that frequently obscures meaning.
• sentences that are disjointed, confusing, or rambling..
"""


CONVENTIONS_RUBURIC = """
Conventions

Score 6: The writing demonstrates exceptionally strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. 
Errors are so few and so minor that the reader can easily skim right over them unless specifically searching for them. 
The writing is characterized by
• strong control of conventions; manipulation of conventions may occur for stylistic effect.
• strong, effective use of punctuation that guides the reader through the text.
• correct spelling, even of more difficult words.
• correct grammar and usage that contribute to clarity and style.
• skill in using a wide range of conventions in a sufficiently long and complex piece.
• little or no need for editing.

Score 5: The writing demonstrates strong control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage) and uses them effectively to enhance communication. 
Errors are few and minor. Conventions support readability. 
The writing is characterized by
• strong control of conventions.
• effective use of punctuation that guides the reader through the text.
• correct spelling, even of more difficult words.
• correct capitalization; errors, if any, are minor.
• correct grammar and usage that contribute to clarity and style.
• skill in using a wide range of conventions in a sufficiently long and complex piece.
• little need for editing.

Score 4: The writing demonstrates control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). 
Significant errors do not occur frequently. 
Minor errors, while perhaps noticeable, do not impede readability. 
The writing is characterized by
• control over conventions used, although a wide range is not demonstrated.
• correct end-of-sentence punctuation; internal punctuation may sometimes be incorrect.
• spelling that is usually correct, especially on common words.
• correct capitalization; errors, if any, are minor.
• occasional lapses in correct grammar and usage; problems are not severe enough to distort meaning or confuse the reader.
• moderate need for editing.

Score 3: The writing demonstrates limited control of standard writing conventions (e.g., punctuation, spelling, capitalization, grammar and usage). 
Errors begin to impede readability.
The writing is characterized by
• some control over basic conventions; the text may be too simple or too short to reveal mastery.
• end-of-sentence punctuation that is usually correct; however, internal punctuation contains frequent errors.
• spelling errors that distract the reader; misspelling of common words occurs.
• capitalization errors.
• errors in grammar and usage that do not block meaning but do distract the reader.
• significant need for editing.

Score 2: The writing demonstrates little control of standard writing conventions. 
Frequent, significant errors impede readability. 
The writing is characterized by
• little control over basic conventions.
• many end-of-sentence punctuation errors; internal punctuation contains frequent errors.
• spelling errors that frequently distract the reader; misspelling of common words often occurs.
• capitalization that is inconsistent or often incorrect.
• errors in grammar and usage that interfere with readability and meaning.
• substantial need for editing.

Score 1: Numerous errors in usage, spelling, capitalization, and punctuation repeatedly distract the reader and make the text difficult to read. 
In fact, the severity and frequency of errors are so overwhelming that the reader finds it difficult to focus on the message and must reread for meaning. 
The writing is characterized by
• very limited skill in using conventions.
• basic punctuation (including end-of-sentence punctuation) that tends to be omitted, haphazard, or incorrect.
• frequent spelling errors that significantly impair readability.
• capitalization that appears to be random.
• a need for extensive editing.
"""

CONVENTIONS_RUBURIC_2 = """
Conventions

Score 3: Consistent, appropriate use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.

Score 2: Adequate use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.

Score 1: Limited use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation for the grade level.

Score 0: Ineffective use of conventions of Standard English for grammar, usage, spelling, capitalization, and punctuation.
"""

PROMPT_ADHERENCE_RUBURIC = """
Prompt Adherence

Score 4: The response is very clear. Supporting evidence is specific to the memoir is used to support the points the writer makes.

Score 3: The response shows a good understanding of the meaning of the text and question, and stays on topic.

Score 2: The response shows an ok-ish understanding of the meaning of the text and question, and occasionally wanders off topic.

Score 1: The response shows a misreading of the text or question, or consistently wanders off topic.

Score 0: The response is irrelevant / incorrect / incomplete.
"""

PROMPT_ADHERENCE_RUBURIC_2 = """
Prompt Adherence
Score 3: The response shows an excellent understanding of the meaning of the text and question, and stays on topic.
Score 2: The response shows a good understanding of the meaning of the text and question, and occasionally wanders off topic.
Score 1: The response shows a misreading of the text or question, or consistently wanders off topic.
Score 0: The response is irrelevant / incorrect / incomplete.
"""

LANGUAGE_RUBURIC ="""
Language

Score 4: Grammar and spelling are excellent, with a wide range of grammatical structures used.
The writing shows evidence of a high range of vocabulary, with words used to good effect in appropriate places.

Score 3: Grammar and spelling are good, with only some minor errors. 
Different kinds of grammatical structures may be used. 
The writing shows evidence of an adequate range of vocabulary.

Score 2: Grammar and spelling show many errors. 
Vocabulary is limited and not very varied. 
Some words may be used in inappropriate places.

Score 1: There are spelling and grammar errors in almost every sentence. 
Vocabulary is extremely limited, leading to repetitive use of words, as well as incorrect use of words, in many places.

Score 0: Too little content to rate.
"""

LANGUAGE_RUBURIC_2 = """
Language

Score 3: Grammar and spelling are excellent, with a wide range of grammatical structures used.
The writing shows evidence of a high range of vocabulary, with words used to good effect in appropriate places.

Score 2: Grammar and spelling are good, with only some minor errors. Different kinds of grammatical structures may be used. 
The writing shows evidence of an adequate range of vocabulary.

Score 1: Grammar and spelling show many errors. Vocabulary is limited and not very varied. Some words may be used in inappropriate places.

Score 0: There are spelling and grammar errors in almost every sentence. 
Vocabulary is extremely limited, leading to repetitive use of words, as well as incorrect use of words, in many places.
"""


NARRATIVITY_RUBURIC = """
Narrativity

Score 4: The response is interesting. 
Proper use of transitional and linking words and sentences makes the narrative flow smoothly. 
The evidence from the memoir supports the points very well.

Score 3: The response is interesting. 
Appropriate use of transitional and linking words and sentences makes the narrative flow smoothly. 
It is often conversational and makes the story easy to follow.

Score 2: The response is somewhat interesting. 
Transitional and linking words are used in some places, but not everywhere.

Score 1: The response is very uninteresting and disjointed and is unable to deliver the content at all.

Score 0: Too little content to rate.
"""

NARRATIVITY_RUBURIC_2 = """ 
Score 3: The response is interesting. Appropriate use of transitional and linking words and sentences makes the narrative flow smoothly. 
It is often conversational and makes the story easy to follow.

Score 2: The response is somewhat interesting. Transitional and linking words are used in some places, but not everywhere.

Score 1: The response is very uninteresting and disjointed and is unable to deliver the content at all.

Score 0: The response is irrelevant / incorrect / incomplete.
"""


VOICE_RUBURIC = """
Voice

Score 6: The writer has chosen a voice appropriate for the topic, purpose, and audience. 
The writer demonstrates deep commitment to the topic, and there is an exceptional sense of “writing to be read.”
The writing is expressive, engaging, or sincere. 
The writing is characterized by
• an effective level of closeness to or distance from the audience (e.g., a narrative should have a strong personal voice, while an expository piece may require extensive use of outside resources and a more academic voice; nevertheless, both should be engaging, lively, or interesting. Technical writing may require greater distance.).
• an exceptionally strong sense of audience; the writer seems to be aware of the reader and of how to communicate the message most effectively. The reader may discern the writer behind the words and feel a sense of interaction.
• a sense that the topic has come to life; when appropriate, the writing may show originality, liveliness, honesty, conviction, excitement, humor, or suspense.

Score 5: The writer has chosen a voice appropriate for the topic, purpose, and audience. 
The writer demonstrates commitment to the topic, and there is a sense of “writing to be read.” 
The writing is expressive, engaging, or sincere. 
The writing is characterized by an appropriate level of closeness to or distance from the audience (e.g., a narrative should have a strong personal voice, while an expository piece may require extensive use of outside resources and a more academic voice; nevertheless, both should be engaging, lively, or interesting. Technical writing may require greater distance.).
• a strong sense of audience; the writer seems to be aware of the reader and of how to communicate the message most effectively. The reader may discern the writer behind the words and feel a sense of interaction.
• a sense that the topic has come to life; when appropriate, the writing may show originality, liveliness, honesty, conviction, excitement, humor, or suspense.

Score 4: A voice is present. 
The writer seems committed to the topic, and there may be a sense of “writing to be read.” 
In places, the writing is expressive, engaging, or sincere. 
The writing is characterized by
• a suitable level of closeness to or distance from the audience.
• a sense of audience; the writer seems to be aware of the reader but has not consistently employed an appropriate voice. The reader may glimpse the writer behind the words and feel a sense of interaction in places.
• liveliness, sincerity, or humor when appropriate; however, at times the writing may be either inappropriately casual or personal, or inappropriately formal and stiff.

Score 3: The writer’s commitment to the topic seems inconsistent. 
A sense of the writer may emerge at times; however, the voice is either inappropriately personal or inappropriately impersonal. 
The writing is characterized by
• a limited sense of audience; the writer’s awareness of the reader is unclear.
• an occasional sense of the writer behind the words; however, the voice may shift or disappear a line or two later and the writing become somewhat mechanical.
• a limited ability to shift to a more objective voice when necessary.
• text that is too short to demonstrate a consistent and appropriate voice.

Score 2: The writing provides little sense of involvement or commitment. 
There is no evidence that the writer has chosen a suitable voice. 
The writing is characterized by
• little engagement of the writer; the writing tends to be largely flat, lifeless, stiff, or mechanical.
• a voice that is likely to be overly informal and personal.
• a lack of audience awareness; there is little sense of “writing to be read.”
• little or no hint of the writer behind the words. There is rarely a sense of interaction between reader and writer.

Score 1: The writing seems to lack a sense of involvement or commitment. The writing is characterized by
• no engagement of the writer; the writing is flat and lifeless.
• a lack of audience awareness; there is no sense of “writing to be read.”
• no hint of the writer behind the words. There is no sense of interaction between writer and reader; the writing does not involve or engage the reader.
"""

STYLE_RUBURIC = """
Style
Score 3: Command of language, including effective and compelling word choice and varied sentence structure, clearly supports the writer's purpose and audience.
Score 2: Adequate command of language, including effective word choice and clear sentences, supports the writer's purpose and audience.
Score 1: Limited use of language, including lack of variety in word choice and sentences, may hinder support for the writer's purpose and audience.
Score 0: Ineffective use of language for the writer's purpose and audience.
"""


OVERALL_SCORE_P1 = """
Overall Score Range : 2 - 12
"""

OVERALL_SCORE_P2 = """
Overall Score Range : 1 - 6
"""

OVERALL_SCORE_P3 = """
Overall Score Range : 0 - 3
"""

OVERALL_SCORE_P4 = """
Overall Score Range : 0 - 3
"""

OVERALL_SCORE_P5 = """
Overall Score Range : 0 - 4
"""

OVERALL_SCORE_P6 = """
Overall Score Range : 0 - 4
"""

OVERALL_SCORE_P7 = """
Overall Score Range : 0 - 30
"""

OVERALL_SCORE_P8 = """
Overall Score Range : 0 - 60
"""


RUBURIC_MAPPER = {
    
    "content": CONTENT_RUBURIC, # for P1, P2, P8
    "content2": CONTENT_RUBURIC_2, # for P5, P6
    "content3": CONTENT_RUBURIC_3, # for P3, P4
    "content4": CONTENT_RUBURIC_4, # for P7

    "organization": ORGANIZATION_RUBURIC, # for P1, P2
    "organization2": ORGANIZATION_RUBURIC_2, # for P7
    "organization3": ORGANIZATION_RUBURIC_3, # for P8
    
    "word_choice": WORD_CHOICE_RUBURIC, # for P1, P2, P8
    
    "sentence_fluency": SENTENCE_FLUENCY_RUBURIC, # for P1, P2, P8
    
    "conventions": CONVENTIONS_RUBURIC, # for P1, P2, P8
    "conventions2": CONVENTIONS_RUBURIC_2, # for P7
    
    "prompt_adherence": PROMPT_ADHERENCE_RUBURIC, # for P5, P6
    "prompt_adherence2": PROMPT_ADHERENCE_RUBURIC_2, # for P3, P4, 

    "language": LANGUAGE_RUBURIC, # for P5, P6
    "language2": LANGUAGE_RUBURIC_2, # for P3, P4, 

    "narrativity": NARRATIVITY_RUBURIC, # for P5, P6
    "narrativity2": NARRATIVITY_RUBURIC_2, # for P3, P4, 

    "style": STYLE_RUBURIC, # for P7
    "voice": VOICE_RUBURIC, # for P8

    "overall1": OVERALL_SCORE_P1,
    "overall2": OVERALL_SCORE_P2,
    "overall3": OVERALL_SCORE_P3,
    "overall4": OVERALL_SCORE_P4,
    "overall5": OVERALL_SCORE_P5,
    "overall6": OVERALL_SCORE_P6,
    "overall7": OVERALL_SCORE_P7,
    "overall8": OVERALL_SCORE_P8,
}


PROMPT_ID_RUBURIC_MAPPER = {
    1 : ["overall1", "content", "organization", "word_choice", "sentence_fluency", "conventions"],
    2 : ["overall2", "content", "organization", "word_choice", "sentence_fluency", "conventions"],
    3 : ["overall3", "content3", "prompt_adherence2", "language2", "narrativity2"],
    4 : ["overall4", "content3", "prompt_adherence2", "language2", "narrativity2"],
    5 : ["overall5", "content2", "prompt_adherence", "language", "narrativity"],
    6 : ["overall6", "content2", "prompt_adherence", "language", "narrativity"],
    7 : ["overall7", "content4", "organization2", "style", "conventions2"],
    8 : ["overall8", "content", "organization3", "word_choice", "sentence_fluency", "conventions", "voice"]
}

OVERALL_SCORE_MAPPER = {
    1 : OVERALL_SCORE_P1,
    2 : OVERALL_SCORE_P2,
    3 : OVERALL_SCORE_P3,
    4 : OVERALL_SCORE_P4,
    5 : OVERALL_SCORE_P5,
    6 : OVERALL_SCORE_P6,
    7 : OVERALL_SCORE_P7,
    8 : OVERALL_SCORE_P8, 
}

for k, v in OVERALL_SCORE_MAPPER.items():
    ruburics = PROMPT_ID_RUBURIC_MAPPER[k]
    ruburics = ruburics[1:]
    ruburics = list(map(lambda ruburic: ''.join([i for i in ruburic if not i.isdigit()]), ruburics))
    OVERALL_SCORE_MAPPER[k] = v + "\n\n Evalucation critera : "+" ".join(ruburics)


def get_ruburic(prompt_id):
    ruburic_list = PROMPT_ID_RUBURIC_MAPPER[prompt_id]
    ruburics_text_list = []
    ruburics_for_prompt = []
    for ruburic in ruburic_list:
        ruburics_text_list.append(RUBURIC_MAPPER[ruburic])
        # remove digit from ruburic
        ruburic = ''.join([i for i in ruburic if not i.isdigit()])
        ruburics_for_prompt.append(ruburic)
    return ruburics_text_list, ruburics_for_prompt