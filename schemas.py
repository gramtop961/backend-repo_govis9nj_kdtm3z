"""
Database Schemas for VoiceForge

Each Pydantic model represents a MongoDB collection. The collection name is the
lowercase of the class name (e.g., DemoRequest -> "demorequest").
"""

from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Literal

class DemoRequest(BaseModel):
    name: str = Field(..., description="Full name of the requester")
    email: EmailStr = Field(..., description="Email address")
    company: Optional[str] = Field(None, description="Company name")
    timeslot: Optional[str] = Field(None, description="Requested time window or slot")
    interest: Optional[str] = Field(None, description="Package interest (Starter/Pro/Enterprise)")
    note: Optional[str] = Field(None, description="Additional notes from the prospect")
    source: Optional[str] = Field("website", description="Lead source tag")

class OnboardingInfo(BaseModel):
    company: str = Field(..., description="Company name")
    url: HttpUrl = Field(..., description="Public website URL")
    hours: Optional[str] = Field(None, description="Business hours information")
    jobs: Optional[str] = Field(None, description="Types of jobs/contracts")
    questions: Optional[str] = Field(None, description="Default questions the agent should ask")
    emergency: Optional[str] = Field(None, description="Emergency and escalation rules")
    contact_email: Optional[EmailStr] = Field(None, description="Main contact email")

class PurchaseIntent(BaseModel):
    plan: Literal["starter", "pro2", "pro3", "enterprise"] = Field(..., description="Selected plan")
    agents: int = Field(..., ge=1, description="Number of agents")
    needDemo: bool = Field(False, description="Whether the buyer also requests a demo")
    email: Optional[EmailStr] = Field(None, description="Buyer email if available")
    company: Optional[str] = Field(None, description="Buyer company if available")

class WorkspacePreference(BaseModel):
    calendar_embed_url: Optional[str] = Field(None, description="Google Calendar embed/appointment URL to show in demo page")
    meet_preferred: bool = Field(True, description="Prefer Google Meet links for demos")
    drive_folder_url: Optional[HttpUrl] = Field(None, description="Folder to drop shared assets")
    allowed_scopes: Optional[List[str]] = Field(None, description="Requested Google Workspace API scopes if OAuth is configured later")

# Example placeholder schemas kept for reference (can be removed later)
class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

class Product(BaseModel):
    title: str
    price: float
    in_stock: bool = True
