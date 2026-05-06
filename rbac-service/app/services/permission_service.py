class PermissionService:
    def has_permission(self, user_role: str, action: str) -> bool:
        """
        Check if a role has permission to perform an action.
        """
        role_permissions = {
            "owner": ["*"],
            "admin": ["read", "write", "delete", "invite"],
            "marketer": ["read", "write", "campaign.create"],
            "viewer": ["read"]
        }
        
        allowed_actions = role_permissions.get(user_role, [])
        
        if "*" in allowed_actions:
            return True
            
        return action in allowed_actions
