# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Membership",
    "category": "G2P",
    "version": "15.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/openg2p/openg2p-registry",
    "license": "Other OSI approved licence",
    "development_status": "Production/Stable",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "mail",
        "contacts",
        "g2p_registry_group",
        "g2p_registry_individual",
        "queue_job",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/registrant_rule.xml",
        "data/group_membership_kinds.xml",
        "data/queue_job_channel.xml",
        "views/groups_view.xml",
        "views/individuals_view.xml",
        "views/group_membership_view.xml",
        "views/group_membership_kinds_view.xml",
        "views/membership_rules.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
