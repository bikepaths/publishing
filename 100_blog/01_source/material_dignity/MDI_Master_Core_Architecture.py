# Repository: ALMU-OS / Master Core Architecture
# Consolidated open-source routing logic for the Material Dignity Infrastructure.

from enum import Enum
from typing import Dict, Any, List, Tuple
import time

# ==========================================
# 1. POPULATION TAXONOMY & MOBILITY
# ==========================================
class PipelineCategory(Enum):
    A_VOLUNTARY = "PIPELINE_A_VOLUNTARY"     # Self-routes to CES; requires standard economic support.
    B_ENGAGEABLE = "PIPELINE_B_ENGAGEABLE"   # Intact survival networks; routes to Communal Dunbar Pods via Warm Offer.
    C_CALCIFIED = "PIPELINE_C_CALCIFIED"     # Anosognosia present; routes to Sovereign Isolation and Compelled Legal Care.
    C_RIPARIAN = "PIPELINE_C_RIPARIAN"       # Severe environmental overlap; requires ACT field extraction and CWA compliance.
    D_NOMADIC = "PIPELINE_D_NOMADIC"         # Active choice; routes to ground-floor harm reduction only (Anti-Detention Covenant).

def classify_population(data: Dict[str, Any]) -> PipelineCategory:
    # Pre-routing check: Classification aborts if basic cultural/linguistic assessment is missing.
    if not data.get("cultural_assessment_complete", False):
        raise ValueError("CULTURAL_ASSESSMENT_REQUIRED: Cannot accurately route without a cultural and linguistic baseline.")

    if data.get("riparian_encampment", False) and data.get("environmental_violation", False):
        return PipelineCategory.C_RIPARIAN
    if data.get("voluntary_nomadic_preference", False) and not data.get("metabolic_destabilization", False):
        return PipelineCategory.D_NOMADIC
    dup = data.get("duration_untreated_psychosis_years", 0)
    anosognosia = data.get("anosognosia_present", False)
    if dup > 3 or anosognosia:
        return PipelineCategory.C_CALCIFIED
    if data.get("functional_social_bonds", False) and data.get("survival_anchors_present", False):
        return PipelineCategory.B_ENGAGEABLE
    return PipelineCategory.A_VOLUNTARY

def evaluate_upward_mobility(client: Dict[str, Any], current_category: PipelineCategory) -> PipelineCategory:
    # Resolves static categorization by providing an upward mobility trajectory.

    # 1. Riparian Extraction Resolution
    if current_category == PipelineCategory.C_RIPARIAN and not client.get("in_wetlands", False):
        if client.get("anosognosia_present", False):
            return PipelineCategory.C_CALCIFIED
        return PipelineCategory.B_ENGAGEABLE

    # 2. Metabolic Healing (C -> B)
    if current_category == PipelineCategory.C_CALCIFIED and client.get("months_stabilized", 0) >= 12:
        if not client.get("anosognosia_present", False):
            return PipelineCategory.B_ENGAGEABLE

    # 3. Economic Reintegration (B -> A)
    if current_category == PipelineCategory.B_ENGAGEABLE and client.get("economic_readiness", False):
        return PipelineCategory.A_VOLUNTARY

    return current_category

# ==========================================
# 2. FIELD ENGAGEMENT & RDI
# ==========================================
class FieldEngagementEngine:
    def __init__(self, target_window_months: int = 18):
        self.target_window_months = target_window_months

    def evaluate_warm_offer_readiness(self, client: Dict[str, Any], network: List[Dict[str, Any]]) -> bool:
        # Linguistic and cultural competency is a baseline prerequisite for engagement.
        if not client.get("cultural_competency_match", True):
            return False

        # Acute crisis necessitates immediate warm offer regardless of 12-month standard.
        if client.get("acute_crisis_window_active", False):
            return True

        if client.get("months_engaged", 0) < 12:
            return False

        if not client.get("trust_established", False):
            return False

        return True

    def map_survival_network(self, client: Dict[str, Any], peers: List[Dict[str, Any]]) -> List[str]:
        return [peer["id"] for peer in peers if peer.get("bond_strength", 0) > 0.7]

# ==========================================
# 3. INTAKE TRIAGE
# ==========================================
class TriageDestination(Enum):
    JAIL = "JAIL_CRIMINAL_ACT"
    ER = "EMERGENCY_ROOM_ACUTE_MEDICAL"
    MS_UNIT = "METABOLIC_STABILIZATION_UNIT"
    GROUND_FLOOR_HARM_REDUCTION = "ZONE_A_HARM_REDUCTION"

class IntakeNeeds(Enum):
    IMMEDIATE_HYGIENE = "SHOWER_AND_CLOTHING"
    IMMEDIATE_NUTRITION = "CALORIC_STABILIZATION"
    IMMEDIATE_REST = "ST_65_ACOUSTIC_SLEEP"
    HARM_REDUCTION = "CLEAN_NEEDLE_EXCHANGE"

def execute_phase_zero_needs_assessment(client_status: Dict[str, Any]) -> List[IntakeNeeds]:
    # Phase Zero entry is unconditional. Services are provided regardless of compliance.
    needs = []
    if client_status.get("days_since_last_shower", 0) > 2:
        needs.append(IntakeNeeds.IMMEDIATE_HYGIENE)
    if client_status.get("caloric_deficit", False):
        needs.append(IntakeNeeds.IMMEDIATE_NUTRITION)
    if client_status.get("sleep_deprivation_hours", 0) > 48:
        needs.append(IntakeNeeds.IMMEDIATE_REST)
    if client_status.get("active_substance_use", False):
        needs.append(IntakeNeeds.HARM_REDUCTION)

    # Baseline standard: Unconditional physiological stabilization
    if IntakeNeeds.IMMEDIATE_HYGIENE not in needs: needs.append(IntakeNeeds.IMMEDIATE_HYGIENE)
    if IntakeNeeds.IMMEDIATE_NUTRITION not in needs: needs.append(IntakeNeeds.IMMEDIATE_NUTRITION)

    return needs

def execute_gate_triage(presentation: Dict[str, Any]) -> TriageDestination:
    # Medical crisis supersedes criminal/legal status.
    if presentation.get("acute_medical_crisis", False) or presentation.get("overdose", False):
        return TriageDestination.ER
    if presentation.get("active_warrant", False) or presentation.get("criminal_act_imminent", False):
        return TriageDestination.JAIL
    if presentation.get("pipeline_category") == PipelineCategory.D_NOMADIC.value:
        return TriageDestination.GROUND_FLOOR_HARM_REDUCTION
    return TriageDestination.MS_UNIT

# ==========================================
# 4. METABOLIC STABILIZATION
# ==========================================
def evaluate_clearance_threshold(patient: Dict[str, Any], days_in_unit: int, current_timestamp: float = None) -> bool:
    if days_in_unit < 30:
        return False

    if current_timestamp is None:
        current_timestamp = time.time()

    data_timestamp = patient.get("last_telemetry_update", 0)
    if (current_timestamp - data_timestamp) > 86400:
        raise ValueError("DATA_STALE: Manual override required. Telemetry exceeds 24-hour confidence threshold.")

    active_sensors = 0
    indicators_met = 0

    if "sustained_hygiene" in patient:
        active_sensors += 1
        if patient["sustained_hygiene"]: indicators_met += 1
    if "sleep_continuity_hours" in patient:
        active_sensors += 1
        if patient["sleep_continuity_hours"] >= 6: indicators_met += 1
    if "consistent_orientation" in patient:
        active_sensors += 1
        if patient["consistent_orientation"]: indicators_met += 1
    if "group_participation" in patient:
        active_sensors += 1
        if patient["group_participation"]: indicators_met += 1
    if "adl_independent" in patient:
        active_sensors += 1
        if patient["adl_independent"]: indicators_met += 1

    if active_sensors == 0:
        return False

    # FLAG: 40% threshold is provisional, requires ML calibration post-deployment.
    return (indicators_met / active_sensors) >= 0.4

# ==========================================
# 5. INTAKE MATCHING ENGINE (SFI)
# ==========================================
class StructuralAssignment(Enum):
    HORIZONTAL_COMMUNAL_POD = "COMMUNAL"
    SOVEREIGN_ISOLATION_UNIT = "SOVEREIGN"
    MEDICAL_HOLD_SECURE_TIER = "5150_SECURE"

class MetricWeight:
    # PROVISIONAL WEIGHT SOURCES:
    # Volatility (0.40): Derived from baseline assault proxies in unmanaged encampments.
    # Cohesion (0.35): Derived from Social Network Analysis (SNA) retention metrics in mutual-aid studies.
    # Solitude (0.25): Derived from environmental psychology metrics on acoustic sanctuary demand.
    # FLAG: Weights are provisional baseline estimates requiring ML calibration post-deployment.
    VOLATILITY = 0.40
    COHESION = 0.35
    SOLITUDE = 0.25

def process_phase_zero_intake(participant_data: Dict[str, Any]) -> Tuple[StructuralAssignment, float]:
    if participant_data.get("is_5150_involuntary", False):
        return StructuralAssignment.MEDICAL_HOLD_SECURE_TIER, 1.0

    vi = float(participant_data.get("volatility_index", 0.0))
    cp = float(participant_data.get("cohesion_propensity", 0.0))
    sd = float(participant_data.get("solitude_demand", 0.0))

    sfi = (vi * MetricWeight.VOLATILITY) + ((1.0 - cp) * MetricWeight.COHESION) + (sd * MetricWeight.SOLITUDE)
    sfi = round(min(max(sfi, 0.0), 1.0), 3)

    if vi >= 0.70 or sfi >= 0.65:
        return StructuralAssignment.SOVEREIGN_ISOLATION_UNIT, sfi
    if sd >= 0.80 and cp <= 0.20:
        return StructuralAssignment.SOVEREIGN_ISOLATION_UNIT, sfi
    return StructuralAssignment.HORIZONTAL_COMMUNAL_POD, sfi

# ==========================================
# 6. LEGAL LEVER SYSTEM
# ==========================================
class LegalInstrument(Enum):
    CARE_COURT = "CARE_COURT_PETITION"               # California Specific
    AOT = "ASSISTED_OUTPATIENT_TREATMENT"            # National (Laura's Law in CA)
    LPS_CONSERVATORSHIP = "SB43_LPS_CONSERVATORSHIP" # California Specific
    GENERAL_CIVIL_COMMITMENT = "INVOLUNTARY_COMMITMENT" # Non-CA Equivalent
    NONE = "VOLUNTARY_PATHWAY"

class TriggeringAuthority(Enum):
    ACT_FIELD_TEAM = "ACT_CLINICIAN"
    PHASE_ZERO_MHRC = "MHRC_PSYCHIATRIST"
    FAMILY_MEMBER = "NEXT_OF_KIN"
    LAW_ENFORCEMENT = "CRISIS_INTERVENTION_TEAM"

def determine_compelled_pathway(client: Dict[str, Any], jurisdiction: str = "CA") -> Tuple[LegalInstrument, TriggeringAuthority]:
    if not client.get("treatment_resistant", False):
        return LegalInstrument.NONE, None
    if client.get("gravely_disabled_profound", False):
        instrument = LegalInstrument.LPS_CONSERVATORSHIP if jurisdiction == "CA" else LegalInstrument.GENERAL_CIVIL_COMMITMENT
        return instrument, TriggeringAuthority.PHASE_ZERO_MHRC
    if client.get("anosognosia_present", False) and client.get("schizophrenia_spectrum", False):
        instrument = LegalInstrument.CARE_COURT if jurisdiction == "CA" else LegalInstrument.GENERAL_CIVIL_COMMITMENT
        return instrument, TriggeringAuthority.ACT_FIELD_TEAM
    if client.get("history_of_noncompliance", False):
        return LegalInstrument.AOT, TriggeringAuthority.ACT_FIELD_TEAM
    return LegalInstrument.NONE, None

# ==========================================
# 7. DUNBAR POD MANAGER
# ==========================================
def validate_pod_capacity(pod_occupants: List[Dict[str, Any]]) -> bool:
    return len(pod_occupants) < 154

def assess_cohesion_anchor_ratio(core_group: List[Dict[str, Any]], current_timestamp: float) -> bool:
    # TEMPORAL DIMENSION: Must be executed on a scheduled CRON interval (e.g., weekly).
    anchors = sum(1 for occupant in core_group if occupant.get("cohesion_propensity", 0) >= 0.8)
    return anchors >= 3

# ==========================================
# 8. DIALECTICAL DIFFUSION
# ==========================================
class DiffusionAction(Enum):
    DE_ESCALATE_SPACE = "ISOLATE_DISRUPTOR"
    DE_LINK_RESOURCES = "CUT_NON_ESSENTIALS"
    VERTICAL_SHIFT = "RELOCATE_72_HOURS"
    STABILIZED = "STABILIZED"

def execute_diffusion_protocol(incident: Dict[str, Any]) -> DiffusionAction:
    if incident.get("horizontal_mediation_failed", False):
        return DiffusionAction.VERTICAL_SHIFT
    if incident.get("resource_abuse", False):
        return DiffusionAction.DE_LINK_RESOURCES
    if incident.get("active_disruption", False):
        return DiffusionAction.DE_ESCALATE_SPACE
    return DiffusionAction.STABILIZED

# ==========================================
# 9. ASSET & COMPANION LOGISTICS (The Three Ps)
# ==========================================
class PetAccommodation(Enum):
    LEVEL_2_KENNEL = "VETERINARY_BOARDING"
    IN_UNIT_APPROVED = "ALMU_COHABITATION"

def process_three_ps(client: Dict[str, Any]) -> Dict[str, Any]:
    logistics = {"pet_status": None, "cart_storage_bay": None, "partner_co_location": False}
    if client.get("has_pet", False):
        if client.get("pet_behavior_certified", False) and client.get("unit_has_capacity", False):
            logistics["pet_status"] = PetAccommodation.IN_UNIT_APPROVED
        else:
            logistics["pet_status"] = PetAccommodation.LEVEL_2_KENNEL
    if client.get("has_cart_possessions", False):
        logistics["cart_storage_bay"] = "ZONE_A_SECURE_STORAGE"
    if client.get("has_bonded_partner", False):
        logistics["partner_co_location"] = True
    return logistics

# ==========================================
# 10. AUTOMATED FACILITY MAINTENANCE
# ==========================================
class MaintenanceState(Enum):
    ROBOTIC_SCRUBBER_DEPLOYED = "GAUSIUM_50_ACTIVE"
    HVAC_PURGE_ACTIVE = "AIR_SCRUB_ACTIVE"
    MAINTENANCE_STANDBY = "STANDBY"

def schedule_cybernetic_maintenance(pod_status: Dict[str, Any]) -> MaintenanceState:
    try:
        # Eliminates punitive chore compliance by automating sanitation
        if float(pod_status.get("bio_load_metric", 0.0)) > 0.7:
            return MaintenanceState.ROBOTIC_SCRUBBER_DEPLOYED
        if float(pod_status.get("air_quality_index", 100.0)) < 90.0:
            return MaintenanceState.HVAC_PURGE_ACTIVE
        return MaintenanceState.MAINTENANCE_STANDBY
    except (ValueError, TypeError):
        return MaintenanceState.HVAC_PURGE_ACTIVE

# ==========================================
# 11. SECURE TRANSIT PROTOCOLS
# ==========================================
class TransitRoute(Enum):
    DIRECT_SALLY_PORT = "SECURE_VAN_TO_SALLY_PORT"
    FIELD_HOLD = "HOLD_IN_FIELD"

def generate_transit_manifest(client: Dict[str, Any]) -> TransitRoute:
    if client.get("warm_offer_accepted", False) and client.get("unit_pre_matched", False):
        return TransitRoute.DIRECT_SALLY_PORT
    return TransitRoute.FIELD_HOLD

# ==========================================
# 12. LABOR PROGRESSION (GARDIEN PIPELINE)
# ==========================================
class VocationalTier(Enum):
    RESIDENT_BASIC = "STABILIZED_RESIDENT"
    CAFE_STEWARD = "CAFE_MAINTENANCE_STEWARD"
    POD_STEWARD_TRAINEE = "GARDIEN_TRAINEE"
    CERTIFIED_PSS = "PEER_SUPPORT_SPECIALIST"

def evaluate_vocational_progression(resident: Dict[str, Any]) -> VocationalTier:
    months_housed = resident.get("months_housed", 0)
    conflict_free_days = resident.get("conflict_free_days", 0)
    if months_housed >= 12 and conflict_free_days >= 180 and resident.get("leadership_aptitude", False):
        return VocationalTier.CERTIFIED_PSS
    if months_housed >= 6 and conflict_free_days >= 90:
        return VocationalTier.POD_STEWARD_TRAINEE
    if months_housed >= 2 and resident.get("metabolic_clearance", False):
        return VocationalTier.CAFE_STEWARD
    # EXPLICIT GUARANTEE: Housing tenure is absolute and NOT contingent on vocational engagement.
    return VocationalTier.RESIDENT_BASIC

# ==========================================
# 13. MEDICAID 1115 WAIVER & ECONOMIC TRIGGERS
# ==========================================
def trigger_medicaid_billing(patient: Dict[str, Any], jurisdiction: str = "CA") -> Dict[str, float]:
    # Generalized Medicaid 1115 Waiver framework. CalAIM is the CA-specific implementation layer.
    billing_ledger = {"CARE_MANAGEMENT_REVENUE": 0.0, "HOUSING_SERVICES_REVENUE": 0.0}
    if patient.get("metabolic_clearance", False):
        billing_ledger["CARE_MANAGEMENT_REVENUE"] += 2500.00
    if patient.get("days_retained", 0) > 30:
        billing_ledger["HOUSING_SERVICES_REVENUE"] += 1800.00
    # INTEGRITY FLAG: Clearance authorization must originate from clinical assessment, never billing state.
    if patient.get("metabolic_clearance", False) and patient.get("days_retained", 0) > 30:
        billing_ledger["INTEGRITY_ALERT"] = "DUAL_TRIGGER_REVIEW_REQUIRED"
    return billing_ledger

# ==========================================
# 14. SURVIVAL PHYSICS (EPISTEMOLOGICAL BASELINE)
# ==========================================
class MoralJustification(Enum):
    COMPELLED_CARE_AUTHORIZED = "ANOSOGNOSIA_DESTROYS_CONSENT"
    VOLUNTARY_ONLY = "AUTONOMY_INTACT"

def evaluate_is_ought_barrier(client: Dict[str, Any]) -> MoralJustification:
    if client.get("anosognosia_present", False) and client.get("duration_untreated_psychosis_years", 0) > 3:
        # Neurological impairment from prolonged untreated psychosis materially compromises informed consent capacity.
        return MoralJustification.COMPELLED_CARE_AUTHORIZED
    return MoralJustification.VOLUNTARY_ONLY

def verify_biological_floor(infrastructure: Dict[str, Any]) -> bool:
    has_secure_sleep = infrastructure.get("st_65_acoustic_isolation", False)
    has_hygiene_access = infrastructure.get("tier_1_comfort_station_access", False)
    return has_secure_sleep and has_hygiene_access

# ==========================================
# 15. PHYSIOLOGICAL TRAUMA METRICS (MATERIAL DIGNITY)
# ==========================================
def calculate_sleep_destruction_damage(sleep_continuity_hours: float, weeks_on_street: int) -> float:
    if sleep_continuity_hours >= 6.0:
        return 0.0
    trauma_index = (6.0 - sleep_continuity_hours) * (weeks_on_street * 1.5)
    return min(trauma_index, 100.0)

def evaluate_nuclear_isolate_risk(social_bonds: int) -> str:
    if social_bonds == 0:
        return "CRITICAL_ISOLATION_OPEN_AIR_TRAUMA_WARD"
    return "SOCIAL_ANCHOR_PRESENT"

# ==========================================
# 16. INSTITUTIONAL CRITIQUE (ARCHITECTURE OF SURVIVAL)
# ==========================================
class HousingModelOutcome(Enum):
    SYSTEMIC_FAILURE = "SCATTERED_SITE_ILLUSION"
    OPERATIONAL_SUCCESS = "VERTICAL_STABILIZATION"

def evaluate_housing_efficacy(model_type: str, client_pipeline: str, peer_support_funded: bool = True) -> HousingModelOutcome:
    if model_type == "SCATTERED_SITE_MARKET_RATE" and client_pipeline in ["PIPELINE_C_CALCIFIED", "PIPELINE_C_RIPARIAN"]:
        return HousingModelOutcome.SYSTEMIC_FAILURE
    if model_type == "VERTICAL_DUNBAR_TOWER":
        if peer_support_funded:
            return HousingModelOutcome.OPERATIONAL_SUCCESS
        return HousingModelOutcome.SYSTEMIC_FAILURE
    return HousingModelOutcome.SYSTEMIC_FAILURE

def calculate_institutional_waste(annual_budget: float, outcomes_audited: bool) -> float:
    # NOTE: 85% waste index and 15% overhead are illustrative parameters derived from
    # the California State Auditor's 2024 report on homelessness spending and HUD OIG efficiency analyses.
    if not outcomes_audited:
        return annual_budget * 0.85
    return annual_budget * 0.15

# ==========================================
# 17. RE-ENTRY CYCLING PATHWAYS
# ==========================================
def process_re_entry(client: Dict[str, Any], current_timestamp: float) -> TriageDestination:
    # Leaving the tower is a recognized cycle, not a systemic failure.
    last_exit = client.get("last_exit_timestamp", 0)
    if (current_timestamp - last_exit) < 604800:  # 7 days
        return TriageDestination.MS_UNIT
    return execute_gate_triage(client)

# ==========================================
# 18. RIPARIAN ENVIRONMENTAL REMEDIATION
# ==========================================
def trigger_cwa_remediation_protocol(encampment_cleared: bool, hazard_level: float) -> str:
    if encampment_cleared and hazard_level > 0.8:
        return "DISPATCH_EPA_BROWNFIELD_TEAM"
    if encampment_cleared:
        return "INITIATE_STANDARD_CWA_RESTORATION"
    return "HOLD_UNTIL_ACT_EXTRACTION_COMPLETE"



