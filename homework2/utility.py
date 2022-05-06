import random
import string


class RandomNameCampaign:

    campaign_name_random = None

    @staticmethod
    def campaign_name():
        if RandomNameCampaign.campaign_name_random is None:
            RandomNameCampaign.campaign_name_random = \
                ("campaign_" + ''.join(random.choice(string.ascii_letters) for i in range(10)))
        return RandomNameCampaign.campaign_name_random


class RandomNameSegment:

    segment_name_random = None
    segment_name_audit = None
    segment_delete_name = None
    segment_delete_audit = None

    @staticmethod
    def segment_name(param):
        if param == "segment_name_random":
            if RandomNameSegment.segment_name_random is None:
                RandomNameSegment.segment_name_random = \
                    ("segment_" + ''.join(random.choice(string.ascii_letters) for g in range(10)))
            return RandomNameSegment.segment_name_random

        if param == "segment_name_audit":
            if RandomNameSegment.segment_name_audit is None:
                segment_name_r = RandomNameSegment.segment_name("segment_name_random")
                RandomNameSegment.segment_name_audit = segment_name_r
            return RandomNameSegment.segment_name_audit + "_audit"

        if param == "segment_delete_name":
            if RandomNameSegment.segment_delete_name is None:
                RandomNameSegment.segment_delete_name = \
                    ("segment_" + ''.join(random.choice(string.ascii_letters) for g in range(10)))
            return RandomNameSegment.segment_delete_name

        if param == "segment_delete_audit":
            if RandomNameSegment.segment_delete_audit is None:
                segment_del_name = RandomNameSegment.segment_name("segment_delete_name")
                RandomNameSegment.segment_delete_audit = segment_del_name
            return RandomNameSegment.segment_delete_audit + "_audit"
