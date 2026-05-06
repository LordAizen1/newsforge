from typing import TypedDict, List


class DigestState(TypedDict):
    raw_articles:    List[dict]
    filtered:        List[dict]
    categorized:     List[dict]
    digest_sections: List[dict]
    email_html:      str
    whatsapp_text:   str
    status:          str
