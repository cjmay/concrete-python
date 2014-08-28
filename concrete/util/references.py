
def add_references_to_communication(comm):
    """Create references for each UUID 'pointer'

    The Concrete schema uses UUIDs as internal pointers between
    Concrete objects.  This function adds member variables to Concrete
    objects that link to the Concrete objects pointed to by the UUIDs.

    For example, each Entity has a 'mentionIdlist' that lists the
    UUIDs of the EntityMentions for that Entity.  This function adds a
    'mentionList' variable to the Entity that is a list of references
    to the actual EntityMention objects.  This allows you to access
    the EntityMentions using:

      entity.mentionList

    This function adds:
    - a 'tokenization' variable to each TokenRefSequence
    - a 'mentionList' to each Entity
    - an 'entityMention' to an Argument if the Argument has an 'entityMentionId'
    - a 'situationMention' to an Argument if the Argument has a 'situationMentionId'
    - a 'mentionList' to a Situation if the Situation has a 'mentionIdList'

    """
#    comm.dependencyParseForUUID = {}
    comm.entityForUUID = {}
    comm.entityMentionForUUID = {}
#    comm.parseForUUID = {}
    comm.sectionForUUID = {}
    comm.sectionSegmentationForUUID = {}
    comm.sentenceForUUID = {}
    comm.sentenceSegmentationForUUID = {}
    comm.situationForUUID = {}
    comm.situationMentionForUUID = {}
    comm.tokenizationForUUID = {}
#    comm.tokenTaggingForUUID = {}

    if comm.sectionSegmentations:
        for sectionSegmentation in comm.sectionSegmentations:
            comm.sectionSegmentationForUUID[sectionSegmentation.uuid.uuidString] = sectionSegmentation
            for section in sectionSegmentation.sectionList:
                comm.sectionForUUID[section.uuid.uuidString] = section
                if section.sentenceSegmentation:
                    for sentenceSegmentation in section.sentenceSegmentation:
                        comm.sentenceSegmentationForUUID[sentenceSegmentation.uuid.uuidString] = sentenceSegmentation
                        for sentence in sentenceSegmentation.sentenceList:
                            comm.sentenceForUUID[sentence.uuid.uuidString]= sentence
                            for tokenization in sentence.tokenizationList:
                                comm.tokenizationForUUID[tokenization.uuid.uuidString] = tokenization

    if comm.entityMentionSets:
        for entityMentionSet in comm.entityMentionSets:
            for entityMention in entityMentionSet.mentionSet:
                comm.entityMentionForUUID[entityMention.uuid.uuidString] = entityMention
                entityMention.tokens.tokenization = comm.tokenizationForUUID[entityMention.tokens.tokenizationId.uuidString]

    if comm.entitySets:
        for entitySet in comm.entitySets:
            for entity in entitySet.entityList:
                comm.entityForUUID[entity.uuid.uuidString] = entity
                entity.mentionList = []
                for mentionId in entity.mentionIdList:
                    entity.mentionList.append(comm.entityMentionForUUID[mentionId.uuidString])

    if comm.situationMentionSets:
        for situationMentionSet in comm.situationMentionSets:
            for situationMention in situationMentionSet.mentionList:
                comm.situationMentionForUUID[situationMention.uuid.uuidString] = situationMention
                for argument in situationMention.argumentList:
                    if argument.entityMentionId:
                        argument.entityMention = comm.entityMentionForUUID[argument.entityMentionId.uuidString]
                    if argument.situationMentionId:
                        argument.situationMention = comm.situationMentionForUUID[argument.situationMentionId.uuidString]
                if situationMention.tokens:
                    situationMention.tokens.tokenization = comm.tokenizationForUUID[situationMention.tokens.tokenizationId.uuidString]

    if comm.situationSets:
        for situationSet in comm.situationSets:
            for situation in situationSet.situationList:
                comm.situationForUUID[situation.uuid.uuidString] = situation
                if situation.mentionIdList:
                    situation.mentionList = []
                    for mentionId in situation.mentionIdList:
                        situation.mentionList.append(comm.situationMentionForUUID[mentionId.uuidString])